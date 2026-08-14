# NLnet Office Hour — 26 August 2026

**Event:** NLnet Office Hour (online)  
**Goal:** Validate Phase 1 strategy before submitting on 3 November 2026  
**Applicant:** Individual, Lithuania (EU)  
**Project:** NativeCAM — open-source CAM for LinuxCNC

## Elevator pitch (30 seconds)

NativeCAM is GPL CAM for LinuxCNC. I maintain the Python 3 port and added lathe cycles and a CI validation suite. I am requesting EUR 6,000 for four weeks to stabilise the baseline — green CI, lathe and Side Drill regression tests, and release docs. This is phase 1 of a four-phase roadmap totalling about EUR 65,000 toward controller-independent G-code and Siemens ISO export.

## Questions to ask

1. **First grant size:** Is EUR 6,000 / 4 weeks appropriate for a first-time individual applicant with existing open-source work (PR merged, validation harness on GitHub)?

2. **Restack fit:** Does conversational CAM for LinuxCNC fit Restack, or should I frame it as open manufacturing infrastructure / digital commons?

3. **Milestone structure:** I plan three milestones (30% / 40% / 30%) tied to CI, feature validation, and release docs. Is this the expected granularity for a EUR 6k project?

4. **Sequential grants:** If Phase 1 succeeds, can I submit Phase 2 (EUR 13k, operation IR + dual post-processor) on the May 2027 deadline, referencing Phase 1 deliverables in the abstract?

5. **Roadmap in attachment:** Is it acceptable to attach a one-page roadmap (Phases 2–4, ~EUR 65k total) without detailed billing, while keeping Phase 1 budget fully detailed?

6. **CodeSupply fallback:** If Restack is not the right call, is CodeSupply (reproducible CI / `.deb` build pipeline) a better angle for the same EUR 6k scope? Should I avoid submitting to both calls in parallel?

7. **Individual applicant:** Any issues submitting as a private individual from Lithuania without a registered company (UAB)?

8. **WCAG / security audit:** At what grant size does NLnet expect WCAG compliance and the security audit service — Phase 2 (~EUR 13k) or Phase 3 (~EUR 20k)?

## Materials to show (screen share if allowed)

- GitHub: https://github.com/cnc-proton/nativecam-py3-gtk3
- PR #6 validation workflow (or main if merged)
- `docs/grants/phase1/attachment-nativecam-phase1.pdf` (4 pages)
- `examples/lathe/xz_profile_demo.xml` — lathe deliverable example

## Notes during call

| Question | Answer |
|----------|--------|
| Restack vs CodeSupply | |
| EUR 6k appropriate? | |
| Sequential grants OK? | |
| Individual from LT OK? | |
| WCAG threshold | |
| Other feedback | |

## Follow-up actions

- [ ] Update abstract based on feedback
- [ ] Adjust milestone percentages if recommended
- [ ] Confirm Restack or switch to CodeSupply
- [ ] Merge PR #6 before submission if still open
