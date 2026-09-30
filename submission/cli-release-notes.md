# AIR — Architecture Workspace 0.1.5 CLI review candidate

Skills-only alternative using the separately installed AIR Engine CLI and its
authenticated local HTTP service. Python, SQLite and local identity remain the
default. Developed by Yannick Huchard, Apache-2.0.

This ZIP has no MCP configuration, credentials, database or embedded engine.
It includes setup/design skills, a scoped CLI helper, reference documentation
and the official logo. The current 0.1.4 MCP distribution remains available.

Validation: 15 local package/helper tests; both skills pass frontmatter validation;
eight synthetic CLI integration cases pass on Windows with public engine rc9.
Three Asteria dossiers retain UNKNOWN/VIOLATED/CONFLICTING, three BLOCKED gates
and nine NOT_EXECUTED business tests. The model simulation is repeatable and
40 handoff files were generated.

[Reviewer guide](https://github.com/yannickhuchard/air-plugin/blob/main/submission/cli-review.md)
and [technical receipt](https://github.com/yannickhuchard/air-plugin/blob/main/submission/cli-review-results.json).

**Not submitted or approved for the OpenAI directory.** Product-specific local
execution eligibility, supported client surfaces and migration of the existing
draft remain pending in support case #16084977. Imported-client prompt testing
and its reviewer recording remain outstanding. No ordinary ChatGPT local CLI
runtime support is implied by this GitHub prerelease. No CI was run.
