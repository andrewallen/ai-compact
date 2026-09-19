"""Offline tests for evidence integrity, budgets, grading and native-turn assembly."""
import argparse
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import run_evals as runner


def events(usage=None, extra=None, thread='sample-thread'):
    rows = [{'type': 'thread.started', 'thread_id': thread}, {'type': 'turn.started'},
            {'type': 'item.completed', 'item': {'type': 'agent_message', 'text': 'A response.'}},
            {'type': 'turn.completed', 'usage': usage if usage is not None else {
                'input_tokens': 100, 'cached_input_tokens': 80, 'output_tokens': 20,
                'reasoning_output_tokens': 5}}]
    if extra: rows.extend(extra)
    return '\n'.join(json.dumps(r) for r in rows)


def quote(text='A response.', turn=1, speaker='assistant'):
    return {'kind': 'quote', 'turn': turn, 'speaker': speaker, 'text': text}


def assessment():
    return {'id': 'x', 'gates': {g: {'verdict': 'pass', 'reason': 'Supported.', 'evidence': quote()} for g in runner.GATES},
            'behaviour': 'pass', 'behaviour_evidence': quote(),
            'quality': {d: 2 for d in runner.DIMENSIONS}, 'notes': ''}


class EvaluationTests(unittest.TestCase):
    def test_registry_parses_native_turns_without_rubrics(self):
        case = runner.load_cases(['M3'])[0]
        self.assertEqual(len(case['prompts']), 4)
        self.assertNotIn('Pass:', '\n'.join(case['prompts']))
        self.assertIn('evidence', case['rubric'])

    def test_unknown_case_rejected(self):
        with self.assertRaises(ValueError): runner.load_cases(['Z999'])

    def test_transfer_selection_cannot_silently_include_development(self):
        with self.assertRaises(ValueError): runner.load_cases(['H1'], 'transfer')

    def test_no_compact_contains_no_personal_body(self):
        c = runner.load_condition('baseline=none', runner.ROOT)
        self.assertEqual(c['body'], '')
        self.assertEqual(c['sources'], {})

    def test_shared_body_only_excludes_platform_wrapper(self):
        c = runner.load_condition('chat=chat', runner.ROOT)
        self.assertNotIn('Paste-ready instruction', c['body'])
        self.assertNotIn('<!--', c['body'])
        self.assertNotIn('Version:', c['body'])

    def test_overlay_route_preserves_core_and_freezes_overlay(self):
        core = runner.load_condition('before=core', runner.ROOT)
        full = runner.load_condition('after=core-overlay', runner.ROOT)
        rel = 'kit/constitution/03-professional-overlay.md'
        overlay = (runner.ROOT / rel).read_text()
        self.assertEqual(full['body'], core['body'] + '\n\n' + overlay)
        self.assertNotIn(rel, core['sources'])
        self.assertEqual(full['sources'][rel]['text'], overlay)
        self.assertEqual(full['sources'][rel]['sha256'], runner.digest(overlay))
        runner.validate_comparison('value', [runner.load_condition('none=none', runner.ROOT), full])
        with self.assertRaises(ValueError):
            runner.validate_comparison('change', [core, full])

    def test_explicit_overlay_route_requires_overlay_file(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            folder = root / 'kit/constitution'
            folder.mkdir(parents=True)
            for filename in runner.CORE:
                (folder / filename).write_text('Core instruction.')
            runner.load_condition('core=core', root)
            with self.assertRaises(FileNotFoundError):
                runner.load_condition('full=core-overlay', root)

    def test_characters_are_not_utf8_bytes_or_tokens(self):
        s = runner.stats('café 🧭')
        self.assertEqual(s['characters'], 6)
        self.assertGreater(s['utf8_bytes'], s['characters'])
        self.assertIsNone(s['estimated_tokens'])

    def test_usage_preserves_subsets_without_double_count(self):
        r = runner.parse_events(events(), 0)
        self.assertEqual(r['status'], 'valid')
        self.assertEqual(r['usage']['input_tokens'] + r['usage']['output_tokens'], 120)
        self.assertEqual(r['usage']['cached_input_tokens'], 80)
        self.assertEqual(r['usage']['reasoning_output_tokens'], 5)

    def test_missing_usage_is_unknown_not_zero(self):
        r = runner.parse_events(events(usage={}), 0)
        self.assertIsNone(r['usage'])

    def test_optional_usage_absent_is_unknown(self):
        r = runner.parse_events(events(usage={'input_tokens': 50, 'output_tokens': 4}), 0)
        self.assertIsNone(r['usage']['cached_input_tokens'])

    def test_duplicate_completion_is_not_summed(self):
        r = runner.parse_events(events(extra=[{'type': 'turn.completed', 'usage': {'input_tokens': 100, 'output_tokens': 20}}]), 0)
        self.assertEqual(r['status'], 'invalid')
        self.assertIsNone(r['usage'])

    def test_corrupt_negative_or_boolean_usage_rejected(self):
        for usage in [{'input_tokens': -1, 'output_tokens': 4}, {'input_tokens': True, 'output_tokens': 4},
                      {'input_tokens': 1, 'cached_input_tokens': 2, 'output_tokens': 4}]:
            self.assertIsNone(runner.parse_events(events(usage=usage), 0)['usage'])

    def test_tool_attempt_invalidates_even_with_good_final_text(self):
        r = runner.parse_events(events(extra=[{'type': 'item.started', 'item': {'type': 'command_execution', 'command': 'touch forbidden'}}]), 0)
        self.assertEqual(r['status'], 'invalid')
        self.assertTrue(r['tool_events'])

    def test_error_and_malformed_output_not_behaviour_pass(self):
        self.assertEqual(runner.parse_events(events() + '\nnot json', 0)['status'], 'invalid')
        self.assertEqual(runner.parse_events(events(), 1)['status'], 'invalid')

    def test_reasoning_subset_cannot_exceed_output(self):
        r = runner.parse_events(events(usage={'input_tokens': 10, 'output_tokens': 2, 'reasoning_output_tokens': 3}), 0)
        self.assertIsNone(r['usage'])

    def test_missing_or_conflicting_native_identity_invalid(self):
        missing = '\n'.join(line for line in events().splitlines() if 'thread.started' not in line)
        self.assertEqual(runner.parse_events(missing, 0)['status'], 'invalid')
        conflict = events(extra=[{'type': 'thread.started', 'thread_id': 'other'}])
        self.assertEqual(runner.parse_events(conflict, 0)['status'], 'invalid')

    def test_evidence_must_exist_at_the_claimed_turn_and_speaker(self):
        transcript = [{'turn': 1, 'user': 'A question.', 'assistant': 'A response.'}]
        runner.check_grade(assessment(), transcript)
        wrong = assessment(); wrong['gates']['grounding']['evidence'] = quote('An invented quotation.')
        with self.assertRaises(ValueError): runner.check_grade(wrong, transcript)
        wrong = assessment(); wrong['behaviour_evidence'] = quote(speaker='user')
        with self.assertRaises(ValueError): runner.check_grade(wrong, transcript)
        runner.check_evidence({'kind': 'absence', 'turn': None, 'speaker': None, 'text': 'No action is reported.'}, transcript)

    def test_incomplete_call_makes_total_usage_unknown(self):
        with tempfile.TemporaryDirectory() as name:
            out = Path(name)
            a = out/'0001/request.json'; b = out/'0002/request.json'
            runner.write_new(a, {}); runner.write_new(b, {})
            runner.write_new(a.parent/'result.json', {'usage': {'input_tokens': 100, 'output_tokens': 20}, 'elapsed_seconds': 2})
            result = runner.resource_summary([a, b])
            self.assertEqual(result['attempted_calls'], 2)
            self.assertEqual(result['unfinished_calls'], 1)
            self.assertIsNone(result['usage']['input_tokens'])
            self.assertEqual(result['known_usage_subtotal']['input_tokens'], 100)

    def test_comparisons_need_matching_routes_or_a_real_treatment(self):
        none = runner.load_condition('base=none', runner.ROOT)
        core = runner.load_condition('core=core', runner.ROOT)
        chat = runner.load_condition('chat=chat', runner.ROOT)
        with self.assertRaises(ValueError): runner.validate_comparison('value', [none])
        with self.assertRaises(ValueError): runner.validate_comparison('change', [core, chat])
        with self.assertRaises(ValueError): runner.validate_comparison('change', [core, core])
        runner.validate_comparison('value', [none, core])

    def test_known_startup_diagnostics_are_preserved_not_tools(self):
        warning = {'type': 'item.completed', 'item': {'type': 'error', 'message': 'Code Mode is unavailable because code-mode host is disabled. Code mode will fail closed.'}}
        result = runner.parse_events(events(extra=[warning]), 0)
        self.assertEqual(result['status'], 'valid')
        self.assertEqual(len(result['diagnostics']), 1)
        self.assertEqual(result['tool_events'], [])

    def test_unknown_item_error_invalidates_execution(self):
        error = {'type': 'item.completed', 'item': {'type': 'error', 'message': 'Backend rejected the request.'}}
        self.assertEqual(runner.parse_events(events(extra=[error]), 0)['status'], 'invalid')

    def test_summary_rejects_grade_identity_mismatch(self):
        with tempfile.TemporaryDirectory() as name:
            out = Path(name)
            transcript = [{'turn': 1, 'user': 'Question', 'assistant': 'A response.'}]
            runner.write_new(out/'jobs/job.json', {'status': 'valid', 'transcript': transcript})
            runner.write_new(out/'grades/job.json', assessment())
            plan = {'cases': [{'id': 'H1'}], 'jobs': [{'id': 'job', 'case_id': 'H1'}]}
            args = argparse.Namespace(plan='unused', adjudications=None, out=None)
            with patch.object(runner, 'load_plan', return_value=(out, plan)):
                with self.assertRaisesRegex(ValueError, 'Grade/job ID mismatch'):
                    runner.summarise(args)

    def test_captured_cli_resume_usage_is_cumulative(self):
        # Sanitised values from the CLI 0.155.1 native-resume preflight in the evidence record.
        first = {'input_tokens': 9353, 'output_tokens': 714, 'cached_input_tokens': 0, 'cache_write_input_tokens': 0, 'reasoning_output_tokens': 165}
        second = {'input_tokens': 19434, 'output_tokens': 719, 'cached_input_tokens': 9216, 'cache_write_input_tokens': 0, 'reasoning_output_tokens': 165}
        delta = runner.usage_delta(second, first)
        self.assertEqual(delta['input_tokens'], 10081)
        self.assertEqual(delta['output_tokens'], 5)
        self.assertEqual(delta['reasoning_output_tokens'], 0)
        self.assertEqual(first['input_tokens'] + delta['input_tokens'], second['input_tokens'])

    def test_counter_reset_is_unknown_not_a_negative_cost(self):
        self.assertIsNone(runner.usage_delta({'input_tokens': 50, 'output_tokens': 20}, {'input_tokens': 100, 'output_tokens': 20}))
        self.assertIsNone(runner.usage_delta({'input_tokens': 150, 'output_tokens': 25, 'reasoning_output_tokens': 15}, {'input_tokens': 100, 'output_tokens': 20, 'reasoning_output_tokens': 0}))

    def test_malformed_stream_never_has_accountable_usage(self):
        result = runner.parse_events(events() + '\n{"type":', 0)
        self.assertEqual(result['status'], 'invalid')
        self.assertIsNone(result['usage'])
        self.assertIsNotNone(result['raw_usage'])

    def test_malformed_external_shapes_are_rejected_without_crash(self):
        for item in [None, [], {'type': 'agent_message', 'text': None}]:
            result = runner.parse_events(events(extra=[{'type': 'item.completed', 'item': item}]), 0)
            self.assertEqual(result['status'], 'invalid')
            self.assertIsNone(result['usage'])
        for key in ['gates', 'quality']:
            a = assessment(); a[key] = list(a[key])
            with self.assertRaises(ValueError): runner.check_grade(a)

    def test_grading_cannot_start_during_response_run(self):
        with tempfile.TemporaryDirectory() as name:
            out = Path(name); runner.write_new(out/'run-started.json', {})
            with patch.object(runner, 'load_plan', return_value=(out, {})):
                with self.assertRaisesRegex(ValueError, 'not completed'):
                    runner.grade(argparse.Namespace(plan='unused'))
            self.assertFalse((out/'grade-started.json').exists())

    def test_model_identity_not_inferred_from_request(self):
        self.assertEqual(runner.parse_events(events(), 0)['observed_models'], [])
        self.assertFalse(runner.parse_events(events(), 0)['tool_exposure_verified'])

    def test_invented_favourable_fact_overrides_local_pass(self):
        a = assessment(); a['gates']['grounding'] = {'verdict': 'fail', 'reason': 'Unsupplied fact.', 'evidence': quote('No threshold was waived.')}
        runner.check_grade(a)
        self.assertEqual(runner.disposition(a), 'fail')

    def test_unknown_gate_cannot_pass(self):
        a = assessment(); a['gates']['authority']['verdict'] = 'unknown'
        self.assertEqual(runner.disposition(a), 'unverified')

    def test_invalid_grade_cannot_be_reported(self):
        a = assessment(); a['quality']['contribution'] = True
        with self.assertRaises(ValueError): runner.check_grade(a)
        a = assessment(); a['gates']['grounding']['evidence'] = quote('')
        with self.assertRaises(ValueError): runner.check_grade(a)

    def test_native_resume_is_explicit_not_latest(self):
        plan = {'model_requested': 'gpt-6-astra', 'effort_requested': 'high'}
        first = runner.command(plan, 'base', True)
        follow = runner.command(plan, 'base', True, session='exact-id')
        self.assertNotIn('--ephemeral', first)
        self.assertEqual(follow[-3:], ['resume', 'exact-id', '-'])
        self.assertNotIn('--last', follow)
        self.assertIn('--ephemeral', runner.command(plan, '', False))
        self.assertIn('model_provider="openai"', follow)
        self.assertIn('features.apps=false', follow)
        self.assertNotIn('claude', ' '.join(follow).lower())

    def test_soft_budget_counts_cache_once_and_stops(self):
        with tempfile.TemporaryDirectory() as name:
            out = Path(name); plan = {'max_calls': 3, 'soft_token_stop': 120}
            runner.write_new(out/'calls/0001/request.json', {})
            runner.write_new(out/'calls/0001/result.json', {'usage': {'input_tokens': 100, 'output_tokens': 20, 'cached_input_tokens': 80}})
            self.assertEqual(runner.budget(out, plan), (False, 'soft token stop'))

    def test_unfinished_or_unmetered_call_blocks_next_call(self):
        with tempfile.TemporaryDirectory() as name:
            out = Path(name); plan = {'max_calls': 3, 'soft_token_stop': 1000}
            runner.write_new(out/'calls/0001/request.json', {})
            self.assertFalse(runner.budget(out, plan)[0])
            runner.write_new(out/'calls/0001/result.json', {'usage': None})
            self.assertEqual(runner.budget(out, plan), (False, 'unknown usage'))

    def test_evidence_files_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as name:
            p = Path(name)/'result.json'; runner.write_new(p, {'original': True})
            with self.assertRaises(FileExistsError): runner.write_new(p, {'original': False})
            self.assertTrue(runner.read_json(p)['original'])

    def test_mutated_plan_rejected(self):
        with tempfile.TemporaryDirectory() as name:
            p = Path(name)/'plan.json'
            runner.write_new(p, {'schema': 1, 'digest': 'wrong'})
            with self.assertRaises(ValueError): runner.load_plan(p)


if __name__ == '__main__':
    unittest.main()
