# AIR plugin — privacy and data handling

Publisher: **Yannick Huchard**. Package: **AIR — Architecture Workspace** (`air-local`). Updated 30 September 2026.

## Package behavior

This public package consists of instructions, references, metadata and a logo. It includes no telemetry collector, analytics SDK, tracking pixel, hosted account service or shared MCP endpoint operated by the publisher. Installing this package does not itself send architecture dossiers to the publisher.

The separate 0.1.5 CLI review candidate also includes a Python helper. It starts
the separately installed AIR CLI as a subprocess against an explicitly selected
local home and loopback HTTP port. It does not read credential contents, collect
telemetry or contact a publisher service. The AIR engine consumes its own protected
credential files. Local CLI results can still enter the agent's conversation.

An agent following the setup skill may read authorized project documentation, configure a local AIR installation and connect the user's chosen MCP service. An agent following the design skill may read and modify architecture dossiers through that service within the user's permissions. The package does not grant access by itself.

## Model and service providers

Content provided in a conversation, files selected by the user and results returned by a connected tool may be processed by the AI platform and model provider. Local AIR storage does not mean that a cloud model processes data locally. The user and their organization control which material is authorized for that platform. The chosen platform's policies and enterprise agreements also apply.

AIR homes, project registries, backups and identities belong to the user's installation. Their retention, access and deletion follow that installation's configuration and the enterprise's rules. Uninstalling the skills package does not delete a separate AIR registry. Never upload credentials, personal data or confidential dossiers to this public repository.

## Support and hosting

GitHub hosts the repository and support issues. Data deliberately posted in public issues is public and subject to GitHub's policies. For plugin questions use [Support](SUPPORT.md). If you need to discuss confidential data, request an appropriate private channel without including that data in the initial public request. No confidential support address is advertised by this package.

Future releases that add hosted services or data collection must describe that behavior before use.
