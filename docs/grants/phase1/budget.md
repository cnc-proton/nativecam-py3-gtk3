# Phase 1 budget — €6,000 / 4 weeks

**Rate:** €45/hour (NLnet cost-recovery)  
**Applicant:** Individual, Lithuania (EU)  
**Programme:** NLnet Restack  
**Duration:** 4 weeks (~130 hours)

## Work breakdown

| Work package | Hours | Rate | Amount |
|--------------|------:|-----:|-------:|
| Lathe XZ stabilization (G71/G72/G73 smoke, ID profile) | 35 | €45 | €1,575 |
| Side Drill validation | 20 | €45 | €900 |
| 4th-axis example sanity | 15 | €45 | €675 |
| CI / `.deb` / pytest | 22 | €45 | €990 |
| VALIDATION.md + release 2.0b-6 | 12 | €45 | €540 |
| Admin + reporting | 8 | €45 | €360 |
| Contingency | 18 | €45 | €810 |
| **Total** | **130** | | **€6,000** |

## Milestone payment schedule

| Milestone | Share | Amount | Week | Deliverables |
|-----------|------:|-------:|------|--------------|
| **M1** | 30% | €1,800 | 1–2 | `.github/workflows/validate.yml` green; pytest + ruff pass; `.deb` builds in CI |
| **M2** | 40% | €2,400 | 2–3 | `cfg/lathe/xz_profile.cfg` smoke-validated; `cfg/mill/drill-side.cfg` validated; tests in `tests/test_validation.py` |
| **M3** | 30% | €1,800 | 4 | `VALIDATION.md`; release tag `2.0b-6`; `examples/mill/4th-axis.xml` sanity documented |

## Ineligible costs (not requested)

- Hardware (CNC machine, probes)
- Proprietary software licenses
- Travel or conference fees
- Subcontractors

## Files touched (expected)

- `cfg/lathe/xz_profile.cfg`, `cfg/lathe/xz_profile_id.cfg`
- `cfg/mill/drill-side.cfg`
- `examples/lathe/xz_profile_demo.xml`
- `examples/mill/4th-axis.xml`
- `.github/workflows/validate.yml`
- `scripts/validate_project.py`, `tests/test_validation.py`
- `VALIDATION.md` (new)
- `debian/changelog` (release 2.0b-6)
