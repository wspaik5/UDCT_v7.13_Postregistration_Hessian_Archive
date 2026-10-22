# UDCT v7.13 Post-registration — Hessian Archive and Reproducibility Audit

**Status:** retrospective execution audit; numerical reproduction **not yet established**. This update does not modify the original scientific report or archived scripts.

## Scope and scientific boundaries

This archive documents Hessian-related sign tests and Jeans physical-admissibility boundaries under specified numerical and physical assumptions. The consolidated original PDF remains authoritative for the precise equations, figures, and reported outcomes. A computational sign or inadmissibility boundary in one implementation is **not** a universal no-go result for MOND or modified gravity.

The archived strict classification is **18 robust-positive, 30 unresolved, 0 robust-negative endpoints**. **Zero of 24** proposed strict sign-transition brackets was validated. The full physical **3-D total-potential Hessian was NOT EVALUATED**. These are *reported archive classifications*, **not independently reproduced results**.

Hydrus I observationally motivated model inputs do **not** constitute a likelihood fit to the complete individual stellar line-of-sight velocity data. Hydrus I-related calculations also predate v7.13.

## Original files (retain unchanged)

- `UDCT_v7.13_Postregistration_Complete_Research_Report_DOI_Linked.pdf` — original consolidated report (not included in this update)
- `UDCT_v7.13_Original_Hessian_Research_Archive.zip` — original archive, reported as 77 Python + 81 JSON + 2 NPZ + 2 TXT (not included in this update)

## Audit update files

- `REPRODUCIBILITY_STATUS.md` — Claude's reported execution findings, qualifications, and follow-up acceptance criteria
- `requirements.txt` — versions used in the reported partial execution check; **not a validated reproduction environment**
- `audit_archive.py` — read-only ZIP inventory and static path/reference scanner, including SHA-256 manifest output
- `VALIDATION_PLAN.md` — sequential validation gates and separate prospective experiments

## What has actually been checked

According to the supplied Claude execution-audit record (2026-10-22), 1/77 scripts completed unmodified; 11 more completed after filename normalization in a scratch copy, for about 12/77 runnable. The outputs were **not compared** to archived JSON results, and B01–B24 six-arm scripts did not run. These findings are **attributed to the supplied audit**, not to a fresh execution in this update.

The present update has **not** rerun the original scripts because the full PDF and ZIP were not supplied with this request. The attached static-audit utility can be run when the ZIP is available.

## First steps

1. Preserve the original PDF/ZIP byte-for-byte and record their SHA-256 hashes.
2. Run `python audit_archive.py path/to/UDCT_v7.13_Original_Hessian_Research_Archive.zip --out audit_results` (Python standard library only).
3. Inspect the inventory and missing references. Obtain original preregistration plan and v7.06/v7.10 inputs; never fabricate missing inputs.
4. Repair paths and filename resolution **only in a separately versioned working copy**, documenting every change.
5. Execute scripts with captured commands, software versions, return codes and outputs; compare outputs to archived JSON with preregistered field-specific tolerances.
6. Only then proceed to B01–B24 convergence tests, full 3-D Hessian and direct Hydrus I stellar-data fits as **new, separately preregistered research**.

## Citation and links

- GitHub: https://github.com/wspaik5/UDCT_v7.13_Postregistration_Hessian_Archive
- Zenodo: https://doi.org/10.5281/zenodo.23539127
- v7.13 preregistration: https://doi.org/10.5281/zenodo.23342971
- v7.12 post-registration: https://doi.org/10.5281/zenodo.23296444

When updating published repositories, label this as a **supplementary reproducibility audit** rather than a replacement of the original scientific result. The existing DOI should be retained only according to the repository's versioning policy.


### Supplementary archive verification

A new read-only cross-check (`verify_saved_evidence.py`, `SAVED_EVIDENCE_CHECK.json`) found a per-target evidence gap: the B18 exploratory JSON is absent and two B19 exploratory JSON files exist. The other 22 uniquely represented targets had internally consistent archived endpoint labels. This is **not** a rerun or confirmation of the published numerical results. See `REPRODUCIBILITY_STATUS.md` before citing complete per-target reproducibility.
