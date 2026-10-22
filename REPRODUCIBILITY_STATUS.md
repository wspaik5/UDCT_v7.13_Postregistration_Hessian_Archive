# UDCT v7.13 — Reproducibility status and verification gates

## Evidence provenance

The counts below are transcribed from the Claude execution check supplied by the researcher, dated **2026-10-22**. The original ZIP and consolidated PDF were **not provided for independent rerun during preparation of this update**. This file therefore records a *reported audit*, not a new confirmation.

## Reported execution environment and results

- Python **3.13.16**, NumPy **2.5.3**, SciPy **1.18.1**; scratch-copy execution with `python -I` and 60–120 s timeouts.
- **77** Python scripts; **1/77** completed as shipped (`Hessian_Equivalent_Density_Audit`).
- **61** scripts reference hardcoded `/mnt/data/...` paths; some require absent files including `preregistration_plan.json`, v7.10/v7.06 sources, and the v7.13 preregistration ZIP.
- **15** scripts expected sibling filenames without the archived timestamp suffix. **11/15** ran after timestamp removal in a scratch copy; four still failed due to missing inputs.
- Approximately **12/77** scripts could run with limited scratch-copy filename changes. This is **not** a claim that their reported numerical outputs were reproduced.
- The B01–B24 six-arm scripts did **not** run because required preregistration-plan inputs were absent.
- **No regenerated numerical outputs were compared with archived JSON**. No published numerical claim has therefore passed a reproduction check.

## Reported scientific status (not independently reverified)

- Strict endpoint classification: **18 robust-positive / 30 unresolved / 0 robust-negative**.
- **0/24** strict sign-transition brackets validated.
- Full physical **3-D total-potential Hessian: NOT EVALUATED**.
- A reported B01 comparison (native-grid minimum approximately −0.159 vs common-radius approximately +0.231) illustrates potential grid dependence; do not interpret it as a verified physical sign transition until the precise definitions, code and arrays have been checked.

## Verification gates (all currently pending in this update)

| Gate | Evidence needed | Current status |
| --- | --- | --- |
| G0 original provenance | Original PDF/ZIP, SHA-256 and manifest | PENDING — files not supplied |
| G1 dependency closure | All required input files and versioned path map | PENDING |
| G2 executable reproduction | Exit code, command, environment, runtime, output log for each script | PENDING |
| G3 numerical reproduction | Field-by-field archived-vs-regenerated JSON/NPZ comparison with predeclared tolerance | PENDING |
| G4 B01–B24 robustness | Matched physical radius, grid refinement, boundaries, all six arms and consistent definitions | PENDING |
| G5 3-D Hessian | Correct total potential, full tensor, derivatives, convergence and consistency tests | NOT EVALUATED |
| G6 observational validation | Hydrus I individual stellar data, selection, membership, uncertainties and likelihood comparison | NOT PERFORMED |

## Immediate engineering fixes — only in a derived working copy

1. Replace absolute paths with a configurable root or `Path(__file__).resolve().parent` where appropriate; avoid silently redirecting to incorrect inputs.
2. Map timestamped filenames through a deterministic manifest instead of renaming or overwriting archived originals.
3. Supply exact missing preregistration and prior-version input files with provenance and hashes.
4. Build a per-script execution manifest and save stdout/stderr, return code, seed, output hashes and timing.
5. Before checking results, declare field-specific absolute/relative tolerances and treatment of NaN/Inf; compare against archived JSON and NPZ outputs.
6. Preserve unsuccessful and ambiguous results; do not upgrade any reported classification without evidence.

## Publication caution

A reproducible *execution* is not the same as reproducible *numerical results*, and neither establishes *physical validity* or *observational agreement*. New convergence tests, 3-D calculations and Hydrus I likelihood fits should be preregistered separately from the retrospective v7.13 audit.


## Additional independent saved-evidence check (2026-10-22)

The supplied original ZIP was read directly (SHA-256: `822177b6b4619e845f1bbd94c285d5c0c1967457490b80fe1151876770cf3335`). The ZIP contains 162 entries: 77 Python, 81 JSON, 2 NPZ and 2 TXT. A read-only independent decision-label recalculation of the individual `Bxx_Six_Arm_Profile_Exploratory` JSON files found **22 uniquely named targets (44 endpoints)** with **17 robust-positive, 27 unresolved, 0 robust-negative**, with no decision-label discrepancies among those 44 endpoints. **B18 has no corresponding per-target exploratory JSON, and B19 has two**. The separate 24-target inventory still reports 24 unresolved brackets and 0 physical Hessian executions. This discrepancy is a **traceability gap**, not evidence that the published 18/30/0 total is false. Do not replace the original aggregate with 17/27/0: the two totals refer to different coverage. Check the B18 source record and both B19 files before claiming complete per-target independent verification. This check recomputed classifications from saved F/E/common-negative fields; it **did not rerun simulations or independently reconstruct F/E from raw profiles**. See `SAVED_EVIDENCE_CHECK.json` and `verify_saved_evidence.py`.
