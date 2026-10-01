# AIR CLI 0.1.6 — submission metadata

Version 0.1.6 supplies English base listing text within current OpenAI submission
limits, French listing translations, a setup onboarding skill and worldwide
availability metadata. The separately installed local engine and executor are
explicit prerequisites. The CLI helper and both skills are byte-identical to the
0.1.5 candidate that passed the eight synthetic technical integration cases.

Package/helper suite: **16 local tests passed**. No CI was run. The new check
rejects oversized public listing text before packaging. The historical 0.1.5
receipt remains unchanged; metadata changes do not create new imported-client
execution evidence or OpenAI approval.

The public source keeps the `air-local` package name. Updating a legacy OpenAI
draft may require its portal-assigned package name. For that upload, only the two
manifest `name` fields are adapted; the skills, helper, logo and other metadata
remain identical. The portal upload hash is recorded separately from the public
archive hash. The existing draft is preserved.

Current official [submission documentation](https://developers.openai.com/plugins/deploy/submission)
states that Skills-only plugins do not need MCP review cases or a demo recording.
The synthetic recipe and videos remain useful supplementary material. The
product-specific local-execution question is disclosed in support case #16084977.
