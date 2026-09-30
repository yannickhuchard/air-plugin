# Official ChatGPT/Codex directory submission

This directory contains preparation material, **not evidence of submission or approval**.

Update on 2026-09-30: developer identity is **Verified** and an AIR — Architecture
Workspace 0.1.4 draft was created. The listing, official verified identity,
Productivity category, public links and icons are saved. It is **not submitted**.
Three starter prompts and release notes are saved too. Both unchanged 0.1.4
skills were uploaded as individual ZIPs and are undergoing OpenAI safety scanning
(up to two hours indicated; no successful scan result claimed).
Follow-up the same day: both `air-local-design` and `air-local-setup` now show
**Passed** in the portal. This is the skill scan result, not directory approval.
Second check the same day: the portal now offers ZIP uploads for new or existing
plugins. The earlier MCP-only form observation is historical. Skills-only plugins
are documented, but AIR's local execution and separately configured MCP dependency
still require eligibility clarification. A demonstration video and public-route
acceptance tests remain required.

Portal check on 2026-09-29: sign-in succeeded, but creating a plugin was blocked
before upload by: "You need a verified developer identity before you can create
or upload a plugin." No draft was created and no package was uploaded. The
publisher has completed the identity check; Organization settings / General /
Verifications now displays "Identity in review". Plugin creation was retried and
remains blocked pending OpenAI approval. The account displayed only the "With MCP" creation route;
eligibility of the local AIR workflow remains unresolved after identity verification.

Next-step material: [OpenAI clarification request](openai-clarification.md),
[demonstration runbook](demo-runbook.md), and the engine's
[second-workstation kit](https://github.com/yannickhuchard/air-engine/blob/main/docs/reception-second-poste.md).
The clarification was sent through authenticated OpenAI support on 2026-09-30,
and escalation to a support specialist was confirmed. A response is pending;
no eligibility approval is claimed.
The public-route video and review cases remain unexecuted until the connection
route is established. Separate [French local demonstration videos](../videos/README.md)
show the product and generated Asteria views; they are not public-route acceptance.

- Public package: AIR — Architecture Workspace 0.1.4, developed by Yannick Huchard.
- Candidate route: a skills package, subject to review of its dependency on local AIR execution and a separately configured MCP connection.
- No universal MCP URL is offered. No developer tunnel or existing integration ID is submitted as a replacement for a supported server.
- The AIR engine and its Asteria fixtures are public at https://github.com/yannickhuchard/air-engine. A reviewer-ready ChatGPT connection still needs to be arranged; public sources alone do not supply a remote review environment.
- Developer identity verification, organization, country availability and policy attestations must be completed in the authenticated portal. They are not inferred from a GitHub profile or local tests.
- The test cases in `test-cases.json` are review scenarios with expected outcomes, not test results.

Official guidance: [Submit plugins](https://developers.openai.com/plugins/deploy/submission) and [Local execution limitations](https://developers.openai.com/plugins/guides/submit-claude-plugin#complete-the-submission-requirements).

OpenAI requires a verified publisher, public listing/support/privacy/terms pages and review. Where core functionality needs local execution, its guidance asks the publisher to contact their OpenAI partner for product-specific review. A public Git repository does not remove this requirement.

Portal: https://platform.openai.com/plugins. Sign in to the organization that will own the listing. Upload the exact released package only through a supported route; resolve scan findings and local-engine eligibility before completing attestations and submitting. After approval, publication is a separate portal action.
