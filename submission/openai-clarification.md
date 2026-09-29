# AIR local deployment — publication route clarification

Status: DRAFT FOR CONTACT, NOT SENT. Prepared 2026-09-30 for Yannick Huchard,
official AIR developer. No partnership or exception is assumed.

Subject: Publication route for AIR — Architecture Workspace, decentralized local MCP

Hello,

I develop AIR — Architecture Workspace, an Apache-2.0 architecture design,
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

The portal exposed only "With MCP", explicitly using the same MCP URL for every
user. Our draft therefore has no MCP URL. We have not substituted a developer
tunnel or disabled authentication to make the form pass.

Could you confirm:

1. The supported directory route for a plugin whose core engine runs on each
   user's workstation, including differences between ChatGPT Chat, ChatGPT Work
   with local execution and Codex.
2. Whether separately configured per-installation MCP connections are supported,
   or require a specific review/enablement. If not, which concrete architecture
   and authentication flow is acceptable without a centralized AIR data service?
3. How this account can use the documented ZIP upload route, and whether the
   existing draft should be migrated rather than duplicated.
4. Which isolated reviewer setup is acceptable for this topology. We can prepare
   five positive/three negative reproducible cases and a walkthrough using only
   the public synthetic fixtures once the supported route is established.

The existing OIDC integration validates external tokens; it is not a complete
ChatGPT OAuth authorization server. We want to implement and test the required
flow only after confirming the supported topology.

Thank you,
Yannick Huchard

## Dispatch notes

Use an existing OpenAI contact if available, or OpenAI support from the account.
Ask for routing to plugin publication/local MCP support; no response or eligibility
is guaranteed. Add the private draft URL/ID from the project receipt when sending.
Do not attach credentials, identity verification documents, account identifiers,
private registries or the Persona link. This public draft contains none of them.

Official references checked on 2026-09-30:
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/guides/submit-claude-plugin#complete-the-submission-requirements

The documentation describes ZIP uploads and asks publishers whose core workflow
requires local execution to contact OpenAI. Account UI availability is distinct
from those general instructions. A skills-only submission is not a workaround
for undisclosed MCP dependencies.
