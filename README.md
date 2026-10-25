# AIR plugin · Architecture Workspace

<img src="plugins/air-local/assets/logo.png" alt="AIR logo" width="112">

**Give your AI assistant a workflow for designing, checking and explaining an architecture.**

AIR connects business needs, user journeys, components, data, decisions and
evidence. These skills guide your assistant through that work, from installation
to the **Projet d’architecture** website and the handoff to builders.
Created by **Yannick Huchard**, under [Apache-2.0](LICENSE).

[Install the plugin](#install-the-published-plugin) ·
[Prepare your agent](docs/agent-quickstart.md) ·
[Engine](https://github.com/yannickhuchard/air-engine) ·
[Support](SUPPORT.md)

## What belongs in each repository?

| Repository | Contains | Install it for |
| --- | --- | --- |
| **air-plugin**, this repository | Skills, manifests, branding and client setup guidance | The assistant's AIR workflow |
| [air-engine](https://github.com/yannickhuchard/air-engine) | Python engine, CLI/API/MCP, examples and technical guides | Model storage, checks, simulations and generated deliverables |
| Your architecture repository | Your sources, drafts, selected baselines and generated files | The actual solution you are designing |

The plugin does not contain the engine, customer data or an authorized server
connection. Install the engine separately and connect the intended project.
Python 3.11+, SQLite and local authentication suffice for the default engine setup.

## Start with a task, not a command catalogue

| You want to | Ask the assistant |
| --- | --- |
| Get started | “Install and connect AIR for this authorized project, then verify the setup.” |
| Design a solution | “Turn these needs into a sourced architecture and explain what is missing.” |
| Review a decision | “Show the alternatives, consequences and evidence behind this choice.” |
| Prepare construction | “Check the component contracts and prepare the versioned builder handoff.” |
| Assess a change | “Compare these exact baselines and identify the evidence to revisit.” |

The two skills are [air-local-setup](plugins/air-local/skills/air-local-setup/SKILL.md)
and [air-local-design](plugins/air-local/skills/air-local-design/SKILL.md).
The assistant prepares the design; the separately installed engine checks the
declared model. A design check does not prove that the future application runs.

## Install the published plugin

The primary package in this repository is **project-MCP skill version 0.1.11**.
Its published companion engine is **0.35.0.dev4**. Verify the installed engine's
catalogue for the features you intend to use. Engine and plugin versions are
independent; [releases](https://github.com/yannickhuchard/air-plugin/releases)
retain their own archives and checksums.

### ChatGPT desktop and Codex CLI

Register the repository marketplace with an installed Codex CLI:

```sh
codex plugin marketplace add yannickhuchard/air-plugin --ref main
codex plugin marketplace list
```

Install `air-local` from **air-official** using the client plugin browser. In
Codex CLI, open `/plugins`; in ChatGPT desktop, open **Plugins**. Start a new
session after installation. For a local checkout instead of a registered Git
source, open the cloned repository as a project: its
`.agents/plugins/marketplace.json` points to `plugins/air-local`.

The [official marketplace guide](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually)
describes local catalogue discovery. The
[client plugin guide](https://learn.chatgpt.com/docs/plugins) describes installation
and supported surfaces. Account and workspace availability still apply.
Registration does not establish a project MCP connection.

### Other agent platforms

A client with a project MCP configuration can connect to AIR using the engine's
[MCP guide](https://github.com/yannickhuchard/air-engine/blob/main/docs/mcp.md).
Use the client's supported skill format or read the skills as the workflow guide.
For Claude Code, this repository also retains a [compatibility marketplace](.claude-plugin/marketplace.json)
and package manifest; use the client's current installation documentation.
Native support depends on the client; a compatible JSON file alone is not a test.

The Codex IDE extension does not install plugins through this plugin browser.
Use a supported desktop/CLI surface for plugin installation, or configure the
engine's CLI/MCP and supported skills directly in the IDE.

### Local CLI candidate and public-directory status

`variants/air-local-cli` preserves the **0.1.7 review candidate** and its historical
submission material. It is separate from the primary project-MCP package and
does not bundle a local executor or the engine. Follow its dated review record;
do not assume it is the newer CLI package described in development discussions.

No successful public OpenAI-directory publication is confirmed by this README.
The [submission records](submission/README.md) are dated observations, not a live
status check. A public GitHub package can be installed through its supported
marketplace route independently of directory publication.

## Connect the engine and begin

1. Follow the [engine installation quickstart](https://github.com/yannickhuchard/air-engine#install-and-verify-the-engine)
   or ask your authorized local agent to install it. Use a dedicated directory.
2. Give setup the engine location, private home, port, credential filename and
   architecture project. The program reads credentials; never paste their values.
3. Configure the project MCP connection and verify its authenticated identity,
   version and filtered tools. A cloud chat needs an authorized remote service;
   it cannot reach your computer by using its own `localhost`.
4. Read the exact project baseline, prepare changes and generate the architecture
   website. An empty installation needs a project first; it does not create your
   business model automatically.

> Use air-local-setup to connect this authorized AIR project. Once verified,
> use air-local-design to develop the architecture, keep sources and decisions,
> identify missing information, run the supported checks and prepare the handoff.

The [agent runbook](docs/agent-quickstart.md) gives platform integrators the setup
inputs, verification sequence and design loop. Video rendering remains optional.

## Data, help and contribution

Keep separate homes and identities for different clients. Local registries do
not automatically synchronize. Use only data your organization permits the
chosen model to process; installation grants no additional business permissions.

For a problem, include the plugin version, engine version, client, connection
mode, failing command/tool and a fictional minimal example in
[an issue](https://github.com/yannickhuchard/air-plugin/issues). Exclude secrets
and customer material. See [SUPPORT.md](SUPPORT.md) for support expectations.

To build the primary package from this repository:

```sh
python scripts/build_plugin.py --output-dir dist/plugin
python -m pytest -q tests/test_plugin_package.py
```

Building produces an archive and SHA-256 receipt; it does not install the engine
or submit a version to a public directory. This documentation update leaves
released archives and historical review packages unchanged. No automatic CI is enabled.

[Package guide](plugins/air-local/README.md) · [Videos](videos/README.md) ·
[License](LICENSE) · [Privacy](PRIVACY.md) · [Terms](TERMS.md)
