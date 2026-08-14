# Phase 2 draft — Architecture seed (EUR 13,000)

**Submit:** 3 May 2027 (only after Phase 1 public + NLnet report)  
**Duration:** 8 weeks (~270 hours)  
**Programme:** NLnet Restack

## Abstract (draft)

Phase 1 of NativeCAM established a validated LinuxCNC baseline (CI, lathe XZ, Side Drill, VALIDATION.md). Phase 2 introduces a minimal Operation IR layer decoupling CAM operations from G-code output, enabling dual export to LinuxCNC NGC (backward compatible) and generic ISO G-code without o-sub calls. Includes 4th-axis indexing validation and five golden-file regression tests.

This is phase 2 of a 4-phase roadmap (~EUR 65k total); phase 3 adds Siemens ISO cycles.

**Request:** EUR 13,000 / 8 weeks

## Budget

| Work package | Hours | EUR |
|--------------|------:|----:|
| Operation IR (minimal dataclasses/JSON) | 55 | 2,475 |
| LinuxCncPost (wrap existing NGC) | 45 | 2,025 |
| IsoGenericPost (basic, no Siemens cycles) | 40 | 1,800 |
| 4th axis indexing validation | 50 | 2,250 |
| Golden-file tests (5 examples) | 35 | 1,575 |
| Docs + admin | 25 | 1,125 |
| Contingency | 20 | 900 |
| **Total** | **270** | **13,000** |

## Milestones

| M | Share | EUR | Deliverable |
|---|------:|----:|-------------|
| M1 | 35% | 4,550 | `nativecam/ir/` module + 2 example operations |
| M2 | 40% | 5,200 | LinuxCncPost + IsoGenericPost + 5 golden tests |
| M3 | 25% | 3,250 | 4th-axis indexing + `docs/post-architecture.md` |

## Prerequisites before submit

- [ ] Phase 1 MoU closed, all payments received
- [ ] Release 2.0b-6 public on GitHub
- [ ] VALIDATION.md linked in abstract
- [ ] WCAG review plan for UI changes in Phase 2

## Scope cuts (vs original ambition)

- No post-processor UI selector in preferences
- No full migration guide — architecture doc only
- IsoGenericPost: basic linear/arc moves, no canned cycles
