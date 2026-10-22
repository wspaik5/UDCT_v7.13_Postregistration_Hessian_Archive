# Validation plan — retrospective audit versus prospective science

## Phase A: make the archived experiment independently inspectable

**A0. Freeze evidence.** Obtain original PDF, original Hessian ZIP, original v7.13 preregistration plan, and all referenced v7.06/v7.10 files. Record checksums, original filenames and release URLs. Do not alter originals.

**A1. Dependency inventory.** Run `audit_archive.py` against original ZIP. Review static findings manually: a string match is not proof of a runtime dependency. Make an exact input-to-script mapping, including file hashes and provenance.

**A2. Portable working copy.** Implement root-relative input paths and a deterministic timestamped-file manifest in a new directory. Keep a machine-readable patch log, with before/after diff and rationale.

**A3. Controlled execution.** Run all 77 entry points in an isolated environment. Record commands, package versions, timeouts, errors, output paths, random seeds, and execution status. No blanket claim of success until individually checked.

**A4. Numerical comparison.** Define per-field comparison rules *before inspecting differences*: numerical absolute/relative tolerances appropriate to each quantity, exact comparison for categorical flags, explicit handling of missing keys, NaNs, infinities and shape changes. Compare all generated JSON/NPZ outputs with archived reference outputs and publish a difference table.

**A5. Classification reconstruction.** Independently regenerate endpoint labels and 24 bracket decisions from original arrays and frozen decision criteria. Report both mismatches and unresolved cases. Do not alter historical claims in place.

## Phase B: new scientific experiments (separate preregistration)

**B1. Grid robustness:** B01–B24 under matched radii, increasing spatial resolution, multiple boundary conditions, finite-difference step sensitivity, interpolation method and error bounds. Examine B01 native-grid −0.159 vs common-radius +0.231 *only after definitions are reconciled*.

**B2. Six-arm consistency:** enforce the same input potential, physical domain, radius sampling and sign convention; distinguish implementation-dependent variation from model-dependent differences.

**B3. Full 3-D total-potential Hessian:** compute all tensor components, verify symmetry and derivative convergence, compare independent differentiation methods and physically meaningful invariants. Do not substitute an equivalent-density proxy for the full Hessian.

**B4. Hydrus I stellar-data likelihood:** obtain the actual publicly available individual velocity measurements, membership probabilities, selection function and measurement uncertainties; specify distance, stellar mass/light model, anisotropy and external-field assumptions. Fit the same dataset with clearly defined Newtonian dark-matter and MOND-like comparators; evaluate goodness of fit and predictive diagnostics with uncertainties.

## Stop / go rules

- If A0/A1 fails, stop claims of numerical reproducibility and publish missing-dependency inventory.
- If A4 fails, preserve failure cases and diagnose them before B1.
- If B1 shows sign reversal from grid changes, classify the bracket as unresolved pending convergence, not a physical boundary.
- If B4 lacks individual stellar data, describe work as observationally motivated simulation, not direct observational validation.

## Deliverables

1. Immutable originals and hash manifest.
2. Portable derived source tree and change log.
3. Per-script execution and numerical-diff reports.
4. B01–B24 robustness tables and plots (only after computation).
5. Separate preregistration and post-registration documents for prospective B-series tests.


### Immediate provenance gate

Before B01–B24 numerical reruns, locate the missing B18 per-target JSON (or document its absence) and determine why two B19 per-target JSON files are archived. Compare their content and hashes, then resolve the correct provenance without overwriting the originals.
