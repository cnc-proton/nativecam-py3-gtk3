# Phase 1 milestone report templates

Use after NLnet approval (expected Q1 2027). Submit payment request per milestone via NLnet portal.

---

## Milestone M1 — CI green (30%, EUR 1,800)

**Period:** Week 1–2  
**Payment request amount:** EUR 1,800

### Deliverables completed

- [ ] `.github/workflows/validate.yml` — all jobs green on `devel`
- [ ] `python3 -m ruff check` — no errors on core modules
- [ ] `python3 scripts/validate_project.py` — passes
- [ ] `python3 -m pytest tests/ -q` — all tests pass
- [ ] `debuild -us -uc -b` — `.deb` artifact produced in CI

### Evidence links

- GitHub Actions run: [URL]
- Commit range: [first]..[last]

### Report text (paste into NLnet payment request)

```
Milestone M1 complete.

Deliverables:
- GitHub Actions workflow validate.yml: static checks, pytest, and Debian package build all pass on every push to devel.
- Ruff lint clean on ncam.py, lathe_polyline.py, pref_edit.py, restore_lcnc.py.
- scripts/validate_project.py passes (INI smoke, lathe demo XML, cfg references).
- pytest suite: N tests passing (attach CI log).

All work under GPL at github.com/cnc-proton/nativecam-py3-gtk3.

Requesting payment of EUR 1,800 (30% of Phase 1 budget).
```

---

## Milestone M2 — Lathe XZ + Side Drill (40%, EUR 2,400)

**Period:** Week 2–3  
**Payment request amount:** EUR 2,400

### Deliverables completed

- [ ] `cfg/lathe/xz_profile.cfg` — G71/G72/G73 cycle options validated
- [ ] `examples/lathe/xz_profile_demo.xml` — loads and passes structural checks
- [ ] `cfg/mill/drill-side.cfg` — Side Drill params validated
- [ ] Tests added/updated in `tests/test_validation.py`
- [ ] NGC subroutine references in cfg exist under `lib/`

### Evidence links

- Test file commits: [URL]
- Example project: examples/lathe/xz_profile_demo.xml

### Report text

```
Milestone M2 complete.

Deliverables:
- Lathe XZ profile (cfg/lathe/xz_profile.cfg): smoke validation for G71/G72/G73 cycle types; xz_profile_demo.xml verified.
- Side Drill (cfg/mill/drill-side.cfg): parameter and NGC path validation added to test suite.
- Extended tests/test_validation.py with regression checks for lathe and side-drill configs.

Requesting payment of EUR 2,400 (40% of Phase 1 budget).
```

---

## Milestone M3 — Release + docs (30%, EUR 1,800)

**Period:** Week 4  
**Payment request amount:** EUR 1,800

### Deliverables completed

- [ ] `VALIDATION.md` — contributor validation guide published
- [ ] Release `2.0b-6` tagged with updated `debian/changelog`
- [ ] `.deb` attached to GitHub Release
- [ ] `examples/mill/4th-axis.xml` — sanity checks documented in VALIDATION.md
- [ ] Final Phase 1 report submitted to NLnet

### Evidence links

- Release: https://github.com/cnc-proton/nativecam-py3-gtk3/releases/tag/2.0b-6
- VALIDATION.md: [URL]

### Report text

```
Milestone M3 complete — Phase 1 final.

Deliverables:
- VALIDATION.md: documents running validation without LinuxCNC (pytest, validate_project.py) and with sim configs.
- Release nativecam 2.0b-6: Debian package and changelog; CI green at tag.
- 4th-axis example (examples/mill/4th-axis.xml): structural sanity checks and documentation for community sim validation.

Phase 1 complete. All outputs GPL on GitHub.

Requesting payment of EUR 1,800 (30% of Phase 1 budget).
```

---

## Phase 1 execution schedule (4 weeks)

| Week | Focus | Hours |
|------|-------|------:|
| 1 | CI hardening, fix any Actions failures | 35 |
| 2 | Lathe XZ tests, submit M1 payment | 35 |
| 3 | Side Drill validation, submit M2 payment | 35 |
| 4 | VALIDATION.md, release 2.0b-6, submit M3 | 25 |

**Total:** ~130 hours @ EUR 45/h = EUR 6,000

## Scope guardrails (do not expand in Phase 1)

- No Operation IR module
- No Siemens post-processor
- No 5-axis simultaneous toolpaths
- No UI post-processor selector

These belong to Phases 2–4 (separate proposals).
