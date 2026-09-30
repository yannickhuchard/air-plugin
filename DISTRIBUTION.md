# Free distribution and ChatGPT access

Updated: 30 September 2026. Official developer: **Yannick Huchard**.

AIR is intended to be freely distributable under Apache-2.0, with architecture
dossiers stored in installations controlled by each architect or enterprise.
SQLite and local authentication remain the default. A shared AIR cloud service
is not part of the initial distribution plan.

## Available today

- This plugin repository and the 0.1.4 package are public.
- The [AIR engine](https://github.com/yannickhuchard/air-engine) is now a separate public distribution, with rc9 sources, installation tools and three synthetic Asteria dossiers. Consult its release validation for the tested scope.
- The plugin is **not submitted or approved** in the official OpenAI directory.
- Publisher identity is verified; a draft is saved and both skills passed automated scanning.
- A [second-workstation reception kit](https://github.com/yannickhuchard/air-engine/blob/main/docs/reception-second-poste.md) is available; its developer-machine rehearsal is distinct from external reception.
- Installing the skills does not install the engine or connect a workstation to ChatGPT.

## Intended routes

| Route | How it works | Remaining work |
| --- | --- | --- |
| Local agentic IDE | Install AIR locally; use CLI or MCP stdio | Actual second-device and native-client acceptance |
| Individually configured ChatGPT connection | An authorized tunnel or reachable HTTPS MCP endpoint connects to the installation | Confirm account support, qualify onboarding and isolation |
| Public ChatGPT directory plugin | Reviewed MCP deployment or explicitly supported local connection | OpenAI eligibility, authentication, review and publication |

Ordinary ChatGPT does not acquire access to your localhost service from a skill.
A ChatGPT Work environment with a local executor must be qualified separately.
An IDE with terminal access can automate the documented installation; web plugin
installation alone does not deploy Python or AIR on a workstation.

The [OpenAI submission process](https://developers.openai.com/plugins/deploy/submission)
supports ZIP uploads and skills-only submissions; remote MCP submissions require
a stable public HTTPS endpoint. A second portal check on 30 September now exposes
the ZIP upload flow, superseding our earlier observation of an MCP-only form.
The [migration guidance](https://developers.openai.com/plugins/guides/submit-claude-plugin)
asks developers to contact OpenAI when the core workflow needs local execution.
This is not a categorical prohibition of every local-use plugin. AIR's current
design skill depends on a separately configured MCP integration, so skills-only
packaging alone does not establish eligibility. A clarification request has been
sent through authenticated OpenAI support; a local CLI-only variant is also part
of the question. No product-specific eligibility approval has been received.

For remote access to private dossiers, the connection must meet the supported
[MCP authentication requirements](https://developers.openai.com/plugins/build/auth).
AIR's local identity and optional OIDC token verifier do not by themselves provide
the complete ChatGPT OAuth onboarding flow. The initial local installation will
continue to work without a mandatory external identity provider.

## Proposed delivery sequence

1. Publish reviewed engine sources and releases without private development history,
   credentials, enterprise materials or documents with unresolved redistribution rights.
2. Receive installation, upgrade, backup and restore on a clean workstation using
   only public downloads and documentation. Announce only tested platforms.
3. Establish the supported per-installation ChatGPT connection route with OpenAI,
   including consent, credential expiry, reconnection and revocation.
4. Run three synthetic architecture dossiers through design, checks, simulation,
   deliverables and continuation in a new conversation. Preserve unknown and failed results.
5. Provide an isolated reviewer environment, execute the review scenarios, submit
   the plugin, then publish it after approval.
6. Validate the guide with an external architect and expand platform support.

These are planned acceptance steps, not completed milestones. The current package
remains 0.1.4; this document does not change its qualification.

## Ownership and costs

The [Apache-2.0 license](LICENSE) permits reuse and redistribution subject to its
conditions. Retain the required license and attribution notices. Architecture
dossiers are not made public or licensed by the engine's software license.
Publisher attribution does not imply OpenAI certification.

AIR's free software license does not include a ChatGPT subscription, domain,
network relay or paid support. ChatGPT availability also depends on the user's
plan, region and workspace policies. Local storage does not mean that no data
leaves the machine: content selected for ChatGPT is sent to the model provider,
and a relay may process traffic. See [Privacy](PRIVACY.md).

No shared public gateway, automatic cross-enterprise synchronization, or universal
ChatGPT availability is promised by this proposal.
