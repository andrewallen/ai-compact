← [Home](../../../README.md) · [Kit](../../README.md) · [Implementation](../README.md) · **Plugins**

# Plugins

Portable distribution wrappers for maintained personal skills. These are implementation-layer packaging; the [skills tracker](../skills/README.md) owns the working set and canonical skill sources.

| Package | Contents |
|---|---|
| [my-voice](my-voice/README.md) | One writing skill and its three companion files, packaged to Agent Plugins 1.0.0. |

[build_my_voice.py](build_my_voice.py) builds and checks the archive and complete releases. [publish_my_voice.py](publish_my_voice.py) publishes verified generated files through ordinary Git history; [test_my_voice.py](test_my_voice.py) exercises packaging and release transitions in temporary repositories.

The [shared catalogue](../../../.claude-plugin/marketplace.json) on `main` points to the generated package on `codex/plugin-marketplace`. The [release workflow](../../../.github/workflows/my-voice-marketplace.yml) validates changes and publishes changed payloads. Generated ZIPs remain ignored in the source checkout. [ADR-013](../../../governance/decisions/adr-013-generated-plugin-marketplace.md) records the distribution boundary and package-version exception; the [marketplace evidence](../../../governance/evidence/2026-09-voice-marketplace.md) records verification limits.
