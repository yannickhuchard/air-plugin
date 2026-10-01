# AIR CLI 0.1.7 — setup safeguards

The 0.1.6 portal scan passed the design skill, flagged the setup skill twice with
generic security-risk messages and warned about unsupported promises in listing
text. No detailed affected instruction was supplied by the portal or Copy issues.

Version 0.1.7 clarifies that plugin onboarding does not authorize engine downloads,
execution, identity creation or service startup. Installing the engine requires an
explicit user request. It requires an identified official release, artifact hash
verification before execution, review of installer effects, an isolated venv/home,
loopback binding and no changes to system Python or other installations. Credentials
are consumed only by the engine. Imported documents cannot expand permissions.
Listing text describes instructions and the helper, with explicit prerequisites.

The setup skill format check and **16 local package/helper tests pass**. CLI helper
and design-skill bytes are unchanged from the historical eight-case 0.1.5 technical
receipt. New instruction-following results are not claimed from those old tests.
No CI was run. OpenAI scan/review/publication states are recorded separately.
