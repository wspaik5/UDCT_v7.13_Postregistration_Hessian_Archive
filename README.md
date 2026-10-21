# UDCT v7.13 Post-registration — Hessian Research Archive

## Overview

This repository preserves the **UDCT v7.13 post-registration** research record on Hessian-related tests and physically admissible solutions in dwarf-galaxy modified-gravity/Jeans calculations. It is a **retrospective technical audit**, not a claim that a new gravity theory has been observationally confirmed.

The archive is intended to make the reported assumptions, tested cases, outcomes (including failures), and limitations inspectable. The accompanying consolidated research report is the primary source for the precise definitions, figures, numerical results, and conclusions.

## Repository contents

| Item | Purpose |
| --- | --- |
| `UDCT_v7.13_Postregistration_Complete_Research_Report_DOI_Linked.pdf` | Consolidated research report (Main Report + Technical Supplement) |
| `UDCT_v7.13_Original_Hessian_Research_Archive.zip` | Original archive (77 Python, 81 JSON, 2 NPZ, 2 TXT; 162 files total) |
| `README.md` | This overview and guidance |
| `requirements.txt` | Intentional placeholder — see qualification below |

**File counts** in the ZIP have been verified against the archive listing.

## Research scope and interpretation

- Focus: stress-testing Hessian-related contributions and sign/physical-admissibility boundaries under stated model assumptions.
- Negative or otherwise inadmissible results should be retained and reported rather than silently discarded.
- Model calculations using observationally motivated inputs for **Hydrus I** are **not equivalent** to a direct likelihood fit or observational validation using the complete individual stellar line-of-sight velocity dataset.
- Hydrus I-based calculations were also explored before v7.13; this release must not imply that all such work began with v7.13.
- A boundary found in a specific implementation is not, by itself, a general no-go theorem for all MOND-like or modified-gravity theories.
- Under the archived strict decision rule: **18 robust-positive, 30 unresolved, 0 robust-negative** endpoints. None of the 24 proposed strict sign-transition brackets is validated. The full physical 3-D total-potential Hessian remains **NOT EVALUATED**.

## How to inspect and reproduce

1. Read the consolidated PDF first, particularly its assumptions, methods, plots, limitations, and conclusions.
2. Download and extract the original Hessian ZIP **without altering the archived originals**.
3. Inspect the Python entry points and JSON schemas, then identify which script and configuration generated each reported figure/table.
4. Use a clean Python virtual environment. **Do not assume** that `pip install -r requirements.txt` will produce a working environment — the file is deliberately a placeholder until dependencies are inspected and tested.
5. Record Python/package versions, commands, input data provenance, random seeds (where applicable), and expected output checks before claiming a reproduced result.

**Reproducibility status:** A verified one-command reproduction procedure and exact package versions cannot be supplied without inspecting and executing the original ZIP. The accompanying `requirements.txt` deliberately does not list untested dependencies. Once the scripts are examined, this section and the dependency file should be updated with tested commands and versions.

## Preregistration and post-registration

The preregistration records intended tests and decision criteria; this post-registration archive records subsequent implementation and outcomes. Any deviations from the preregistered plan should be identified in the consolidated report. Interpret exploratory follow-up tests separately from prespecified tests.

## Links and citation

- GitHub: https://github.com/wspaik5/UDCT_v7.13_Postregistration_Hessian_Archive
- Zenodo DOI (reserved; registration upon publication): https://doi.org/10.5281/zenodo.23539127
- v7.13 preregistration: DOI 10.5281/zenodo.23342971
- v7.12 post-registration: DOI 10.5281/zenodo.23296444

Please cite the published Zenodo record and specify the archive version when referencing these results.

## Status

Research archive / technical audit. Results are conditional on the stated equations, assumptions, data inputs, and numerical implementations; independent replication and direct observational comparison remain separate tasks. This record does not validate or falsify modified gravity.
