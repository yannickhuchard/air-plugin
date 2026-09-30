# AIR local deployment — publication route clarification

Status: SENT through authenticated help.openai.com support on 2026-09-30,
on behalf of Yannick Huchard, official AIR developer. Human escalation confirmed.
This public record summarizes the request without private portal identifiers.
No partnership, exception or eligibility approval is assumed.

Subject: Publication route for AIR — Architecture Workspace, decentralized local MCP

Hello,

I am contacting you on behalf of Yannick Huchard, developer of AIR — Architecture
Workspace, an Apache-2.0 architecture design,
verification and simulation tool. My developer identity is verified, and a 0.1.4
draft exists in the OpenAI plugin portal. Both uploaded skills passed the portal's
automated safety scan. This is not a claim of directory approval.

Each architect or enterprise installs the Python engine on its own workstation,
with SQLite and a local identity. PostgreSQL and OIDC are optional independent
features. There is no shared hosted AIR service. Each registry has its own
permissions and data; installations do not imply automatic federation or sync.
The modeled business applications are not executed by AIR.

Public engine and three synthetic Asteria dossiers:
https://github.com/yannickhuchard/air-engine
Public skills, license, privacy policy and terms:
https://github.com/yannickhuchard/air-plugin

The legacy portal exposed only "With MCP", using the same MCP URL for every user.
A second check on 30 September now exposes the documented ZIP upload route for
new or existing plugins. The existing draft still has incomplete MCP configuration
and no package version selected. The earlier observation is historical, not a
general prohibition of local-use plugins. We have not substituted a developer
tunnel or disabled authentication to make the form pass. The current design skill
needs a separately installed engine and project-specific MCP; that dependency
will be disclosed, not disguised as a self-contained skills-only package.

Could you confirm:

1. The supported directory route for a plugin whose core engine runs on each
   user's workstation, including differences between ChatGPT Chat, ChatGPT Work
   with local execution and Codex.
2. Whether separately configured per-installation MCP connections are supported,
   or require a specific review/enablement. If not, which concrete architecture
   and authentication flow is acceptable without a centralized AIR data service?
   Could a local CLI-only skills variant receive product-specific review instead?
3. How to migrate the existing draft with Upload new version rather than create
   a duplicate, and handle its incomplete MCP configuration if a local CLI route
   is agreed.
4. Which isolated reviewer setup is acceptable for this topology. We can prepare
   five positive/three negative reproducible cases and a walkthrough using only
   the public synthetic fixtures once the supported route is established.

The existing OIDC integration validates external tokens; it is not a complete
ChatGPT OAuth authorization server. We want to implement and test the required
flow only after confirming the supported topology.

Thank you,
Yannick Huchard

## Dispatch notes

The request was sent in the signed-in account's official support chat, with the
existing OpenAI draft identifier. No credentials, verification documents, private
registries or Persona link were sent. This public record excludes the draft ID.

AI-assisted support initially answered with general public HTTPS MCP requirements
and asked whether the target was the public directory or managed/Git distribution.
We confirmed the public directory and requested a human specialist because the
question concerns the documented local-execution product-specific review and a
possible CLI-only skills variant. The automated answer is not treated as a human
eligibility ruling or as approval.

The support UI then confirmed escalation to a specialist, with a response expected
in the coming days and replies also sent by email. No case number was displayed.
Product-specific eligibility remains pending; the plugin is not submitted or approved.

Official references checked on 2026-09-30:
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/guides/submit-claude-plugin#complete-the-submission-requirements

The documentation describes ZIP uploads and asks publishers whose core workflow
requires local execution to contact OpenAI. Account UI availability is distinct
from those general instructions. A skills-only submission is not a workaround
for undisclosed MCP dependencies.
