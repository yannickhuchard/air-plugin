# Local CLI package — product-specific review preparation

Support case **#16084977**, reply from **Paul**, read on 30 September 2026.
The specialist confirms that local execution is not categorically ineligible and
recommends preparing a Skills-only AIR CLI variant for product-specific review.
This is guidance to prepare, not eligibility approval or acceptance of a submission.

## Package and prerequisites

Source: `variants/air-local-cli`, public `air-local` identity, current version 0.1.7.
The historical technical receipt below covers 0.1.5. The helper/design-skill bytes
remain identical; setup safeguards and listing metadata changed in 0.1.7.
Build: `python scripts/build_plugin.py --variant cli --output-dir dist/cli`.
The existing 0.1.4 MCP distribution and directory draft are preserved.
The CLI ZIP contains the two skills, their helper/resources, manifests, logo and
license. No engine, tokens, runtime database or MCP configuration is included.

The reviewer needs a local execution surface, Python 3.11+, an independently
installed public AIR Engine 0.34.0rc9 in its `.venv`, write access to a new local
review directory, and loopback HTTP access. Windows/Python 3.12 is the reception
platform; other platforms/surfaces need their own execution evidence.
Follow the engine README, installation and validation documents, with the public
release hashes. No company account, production credentials, public backend or
developer workstation access is required. First installation may fetch pip packages.

The CLI uses AIR's existing authenticated HTTP API on 127.0.0.1. This is **not an
embedded/in-process engine** and it does not remove AIR's local authentication.
The helper requires explicit engine, home and port, and supports the design
commands. The engine reads protected credential files; the agent must not print
them. Configuration is owned by the separate engine installation, not a plugin
credential store. That dependency remains explicitly subject to OpenAI review.

## Reproduce the technical checks

After installing the engine, from the plugin checkout:

```text
python submission/rehearse_cli.py --engine <absolute-engine-checkout> --output <new-local-review-directory>
```

The script creates a unique SQLite home, synthetic local administrator and reader,
starts an isolated loopback service, exercises the packaged helper and stops only
that service in a finally block. It refuses AIR_DATABASE_URL. Its `run-*` directories
contain protected synthetic credentials and must stay outside Git and recordings.
It reuses the installed venv: this is not itself proof of a clean engine installation.
The public engine's separate `receive_public.py` kit covers clean installation.

| Case | Expected result |
| --- | --- |
| CLI-P1 | Authenticated identity and available capabilities |
| CLI-P2 | Three Asteria dossiers: UNKNOWN, VIOLATED, CONFLICTING; three BLOCKED gates and nine NOT_EXECUTED business tests; actual HTML views |
| CLI-P3 | Valid change preparation with original baseline digest unchanged |
| CLI-P4 | Seeded repeatable latency simulation qualified DECLARED_MODEL_SIMULATION |
| CLI-P5 | Actual generated engineering handoff files citing pinned baselines |
| CLI-N1 | Missing engine: actionable error, no execution |
| CLI-N2 | Missing configuration: actionable error, no fabricated success |
| CLI-N3 | Synthetic reader cannot write (HTTP 403) |

These are **technical integration cases**, distinct from the original agent prompt
cases in `test-cases.json`. Their execution does not certify instruction following,
prompt-injection resistance, an imported plugin, a second physical workstation,
or a newly supported ChatGPT surface. The original cases remain unexecuted for
public submission until tested in the agreed client with the imported package.

## Submission and next steps

On 1 October 2026, **0.1.7 was formally submitted** into the existing draft.
Both skill scans passed and the package detail page shows **In review**.
Only the two manifest names were adapted to the legacy portal-assigned identity.
The CLI archive has no MCP configuration. The portal's existing MCP warning and
category warning did not block submission. [Record](openai-upload-2026-10-01.json).

Technical rehearsal on 30 September 2026: **8/8 PASS_SCOPED** on Windows using
the separately installed public rc9 engine. [Receipt](cli-review-results.json).
The three dossiers retain their expected blocked outcomes; 40 handoff files were
generated. The declared latency model gives p95 = 200 ms for a 500 ms target,
identically across two calls. This is a model result, not measured application latency.
The package/helper tests also pass: **15 tests**, without CI. Both skill frontmatter
checks pass. These checks do not replace the client and directory steps below.

1. Await the review decision and local-execution eligibility feedback. Listing
   approval remains distinct from runtime availability on a particular client.
2. If OpenAI requests client evidence for the product-specific review, run the
   imported skills in the agreed clean client with synthetic data and record the
   actual results separately from the existing technical CLI receipt.
3. Supply a real client walkthrough if requested. The current official submission
   documentation does not require MCP review cases or a demo recording for a
   Skills-only plugin. Earlier preparation notes treated these too broadly.
4. Publish the approved version after acceptance. Do not claim ordinary ChatGPT
   can execute local CLI without a local executor.

The two [public product videos](../videos/README.md) explain AIR and Asteria.
They are supplemental materials, not the imported-client reviewer recording.
