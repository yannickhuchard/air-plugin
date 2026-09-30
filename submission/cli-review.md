# Local CLI package — product-specific review preparation

Support case **#16084977**, reply from **Paul**, read on 30 September 2026.
The specialist confirms that local execution is not categorically ineligible and
recommends preparing a Skills-only AIR CLI variant for product-specific review.
This is guidance to prepare, not eligibility approval or acceptance of a submission.

## Package and prerequisites

Source: `variants/air-local-cli`, same `air-local` identity, candidate version 0.1.5.
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

## Remaining reviewer sequence

Technical rehearsal on 30 September 2026: **8/8 PASS_SCOPED** on Windows using
the separately installed public rc9 engine. [Receipt](cli-review-results.json).
The three dossiers retain their expected blocked outcomes; 40 handoff files were
generated. The declared latency model gives p95 = 200 ms for a 500 ms target,
identically across two calls. This is a model result, not measured application latency.
The package/helper tests also pass: **15 tests**, without CI. Both skill frontmatter
checks pass. These checks do not replace the client and directory steps below.

1. Obtain confirmation of eligible local execution surfaces and how to convert
   the existing legacy draft in place. Do not create a duplicate listing.
2. Upload the candidate to that existing draft through the confirmed path; run
   new scans. The 0.1.4 Passed scans do not cover the changed 0.1.5 skills.
3. In the agreed clean reviewer setup, invoke the imported skills with the five
   positive/three negative user prompts. Use the CLI equivalents, local synthetic
   project and generated exact references; record actual outcomes separately.
4. Record a real client walkthrough of installation/preflight, baseline review,
   change preparation, simulation and handoff, including a prerequisite/access
   refusal. Keep credentials and unrelated screen content out of the recording.
5. Submit only after those prerequisites are met. A public listing is distinct
   from runtime availability. Do not claim ordinary ChatGPT can execute local CLI.

The two [public product videos](../videos/README.md) explain AIR and Asteria.
They are supplemental materials, not the imported-client reviewer recording.
