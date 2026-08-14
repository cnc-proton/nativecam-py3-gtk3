# Phase 3 draft — Siemens ISO subset (EUR 20,000)

**Submit:** 3 November 2027 (after Phase 2 deliverables public)  
**Duration:** 10 weeks (~440 hours)  
**Programme:** NLnet Restack

## Abstract (draft)

NativeCAM Phase 2 delivered an Operation IR with LinuxCNC and generic ISO post-processors. Phase 3 adds SiemensIsoPost for 808D/828D ISO mode: mill drill cycles (G81–G83 to CYCLE82/83), lathe roughing (G71 to CYCLE95 subset), Side Drill plane/rotation mapping, and dual-output (one project, LinuxCNC + Siemens files). Includes example projects and response to NLnet security audit.

Pitch: EU digital sovereignty — workshops run the same open CAM project on LinuxCNC or Siemens without proprietary CAM.

**Request:** EUR 20,000 / 10 weeks

## Budget

| Work package | EUR |
|--------------|----:|
| SiemensIsoPost core | 4,500 |
| Mill drill cycles (CYCLE82/83) | 2,700 |
| Lathe roughing (CYCLE95 subset) | 3,150 |
| Side Drill Siemens mapping | 2,250 |
| Examples + dual-output build | 2,700 |
| Security audit response + admin | 2,700 |
| Contingency | 2,000 |
| **Total** | **20,000** |

## Milestones

| M | Share | EUR | Deliverable |
|---|------:|----:|-------------|
| M1 | 30% | 6,000 | SiemensIsoPost skeleton + mill drill CYCLE82 |
| M2 | 45% | 9,000 | Lathe G71→CYCLE95 + Side Drill plane/rotation |
| M3 | 25% | 5,000 | `examples/siemens/` + dual-output + audit fixes |

## Scope limits

- 808D/828D ISO mode only — not full Sinumerik dialect
- Subset of cycles — not complete parity with LinuxCNC feature set
- Security audit via NLnet service (budget admin line)

## Prerequisites

- [ ] Phase 2 golden-file tests passing on `main`
- [ ] `docs/post-architecture.md` published
- [ ] Request NLnet security audit early in Phase 3
