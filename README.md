# AIR — Architecture Workspace

<img src="plugins/air-local/assets/logo.png" alt="AIR architecture mark" width="128">

Official architecture workflow plugin by **Yannick Huchard**. Apache-2.0.

[Présentation et parcours vidéo des trois dossiers Asteria (français)](videos/README.md).

**Local CLI review candidate:** [Skills-only variant 0.1.5](variants/air-local-cli/README.md)
and [review procedure](submission/cli-review.md), prepared following specialist
guidance in case #16084977. Public-directory eligibility and migration of the
existing draft remain pending. The 0.1.4 distribution below is unchanged.

Design, verify, simulate and prepare architecture dossiers for engineers, project managers and operations using an AIR installation controlled by your enterprise. AIR means Architecture Intermediate Representation. The stable plugin identifier is `air-local`; this public package is **0.1.4**.

## What is public, and what is required

This repository contains the plugin's two skills, logo, manifests, license, packaging code and public documentation. It contains no enterprise data, tokens, runtime database, private repository history or shared MCP server.

**The AIR engine is a separate public prerequisite:** [sources and releases](https://github.com/yannickhuchard/air-engine). Install a reviewed engine release and explore the three included synthetic Asteria dossiers. For a dossier workflow, connect your organization's AIR MCP service separately. Installing this plugin does not grant engine access or automatically connect a workstation to ChatGPT.

For ChatGPT, a local stdio MCP process is not a remote connection. Your organization needs an authorized remote MCP connection and a deployment accepted by the client. The current plugin is not listed or approved in the official ChatGPT/Codex directory. Its local-engine dependency requires review for that publication channel.

## Install the public package

See the [free distribution and ChatGPT access assessment](DISTRIBUTION.md) for
the proposed public-engine rollout and the remaining connection and review requirements.

Download the ZIP and `plugin-package.json` from [Releases](https://github.com/yannickhuchard/air-plugin/releases). Verify the ZIP's SHA-256 before extracting the `air-local` folder. Install it through your client's supported local-plugin flow.

For a Git marketplace in Codex:

```text
codex plugin marketplace add yannickhuchard/air-plugin --ref main
codex plugin add air-local@air-official
```

The catalog is `.agents/plugins/marketplace.json`. Availability of local/Git marketplaces varies by client; this command does not publish to the universal directory. Open a new conversation after installation. Do not copy credentials or enterprise data into the plugin directory.

Example prompt: “Use AIR to review the architecture dossier in this project's configured registry.” If the engine or connection is missing, the plugin reports that prerequisite rather than inventing a result.

## Development

Python 3.11+ builds the ZIP with no third-party dependency:

```text
python scripts/build_plugin.py --output-dir dist/plugin
```

Packaging tests use pytest: `python -m pytest -q tests/test_plugin_package.py`. No CI workflow is enabled. Engine versions, engine qualification and plugin versions are separate; package installation is not production or normative qualification.

[Plugin instructions](plugins/air-local/README.md) · [Privacy](PRIVACY.md) · [Terms](TERMS.md) · [Support](SUPPORT.md) · [Submission preparation](submission/README.md)
