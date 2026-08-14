# NativeCAM Phase 1 — NLnet attachment (PDF source)

*Convert to PDF with `python3 docs/grants/build_attachment_pdf.py`*

---

## 1. Project summary

**NativeCAM** is a GPL conversational CAM GUI for LinuxCNC (Python 3, GTK3). Maintainer: CNC Proton. Repository: https://github.com/cnc-proton/nativecam-py3-gtk3

**Phase 1 goal:** Stabilise the LinuxCNC baseline with automated validation, lathe XZ profile regression, Side Drill checks, and release documentation.

**Request:** €6,000 / 4 weeks / 130 hours @ €45/h  
**Applicant:** Individual, Lithuania (EU)

---

## 2. Phase 1 budget and milestones

| Work package | Hours | € |
|--------------|------:|--:|
| Lathe XZ stabilization | 35 | 1,575 |
| Side Drill validation | 20 | 900 |
| 4th-axis example sanity | 15 | 675 |
| CI / deb / pytest | 22 | 990 |
| VALIDATION.md + release 2.0b-6 | 12 | 540 |
| Admin + reporting | 8 | 360 |
| Contingency | 18 | 810 |
| **Total** | **130** | **6,000** |

| Milestone | € | Deliverable |
|-----------|--:|-------------|
| M1 (30%) | 1,800 | CI green: Actions, pytest, `.deb` build |
| M2 (40%) | 2,400 | Lathe XZ + Side Drill validated with tests |
| M3 (30%) | 1,800 | VALIDATION.md, release 2.0b-6, 4th-axis sanity |

---

## 3. Four-phase roadmap (future proposals — not part of Phase 1 contract)

| Phase | Amount | Weeks | Scope | Target submit |
|-------|-------:|------:|-------|---------------|
| **1** (this) | €6,000 | 4 | Stabilize LinuxCNC baseline, CI, docs | Nov 2026 |
| **2** | €13,000 | 8 | Operation IR + dual post (LinuxCNC + generic ISO) + 4th axis | May 2027 |
| **3** | €20,000 | 10 | Siemens ISO subset (808D/828D), dual-output | Nov 2027 |
| **4** | €26,000 | 12 | 5-axis indexing, lathe completion, i18n, packaging | May 2028 |
| **Total** | **~€65,000** | **34** | Multi-controller open CAM stack | — |

Each phase is a separate NLnet proposal after public deliverables of the previous phase.

---

## 4. Architecture (future phases — dashed = not in Phase 1)

```
  Feature configs (.cfg)     Operation IR (Phase 2)     Post-processors
  lathe/xz_profile.cfg  -->  JSON/dataclasses      -->  LinuxCncPost
  mill/drill-side.cfg                               -->  IsoGenericPost (Ph.2)
                                                    -->  SiemensIsoPost (Ph.3)
```

Phase 1 validates existing Feature → NGC path only.

---

## 5. Prior work and links

- **Lathe XZ profiles:** G71/G72/G73 on `devel` branch — `cfg/lathe/xz_profile.cfg`, `examples/lathe/xz_profile_demo.xml`
- **Side Drill:** `cfg/mill/drill-side.cfg` — horizontal spindle drilling (Top/Bottom/Left/Right)
- **Validation harness:** PR #6 — `scripts/validate_project.py`, `.github/workflows/validate.yml`, 40+ pytest tests
- **4th axis demo:** `examples/mill/4th-axis.xml` (community validation pending)
- **License:** GPL. **Platform:** Debian 13, LinuxCNC 2.9+

**YouTube / community:** LinuxCNC forum, CNC Proton channel

---

*End of attachment — 4 pages when rendered*
