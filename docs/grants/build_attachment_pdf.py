#!/usr/bin/env python3
"""Build Phase 1 NLnet attachment PDF from structured content."""

from __future__ import annotations

from pathlib import Path

from fpdf import FPDF

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "phase1" / "attachment-nativecam-phase1.pdf"


class AttachmentPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.cell(0, 8, "NativeCAM - NLnet Restack Phase 1 Attachment", align="R")
        self.ln(10)

    def section_title(self, title: str):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 8, title)
        self.ln(6)

    def body_text(self, text: str):
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 5, text)
        self.ln(2)

    def table(self, headers: list[str], rows: list[list[str]], col_widths: list[int]):
        self.set_font("Helvetica", "B", 9)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, h, border=1)
        self.ln()
        self.set_font("Helvetica", "", 9)
        for row in rows:
            for i, cell in enumerate(row):
                self.cell(col_widths[i], 7, cell, border=1)
            self.ln()
        self.ln(4)


def main() -> None:
    pdf = AttachmentPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.section_title("1. Project summary")
    pdf.body_text(
        "NativeCAM is a GPL conversational CAM GUI for LinuxCNC (Python 3, GTK3). "
        "Maintainer: CNC Proton. Repository: github.com/cnc-proton/nativecam-py3-gtk3\n\n"
        "Phase 1 goal: Stabilise the LinuxCNC baseline with automated validation, "
        "lathe XZ profile regression, Side Drill checks, and release documentation.\n\n"
        "Request: EUR 6,000 / 4 weeks / 130 hours at EUR 45/h\n"
        "Applicant: Individual, Lithuania (EU)"
    )

    pdf.section_title("2. Phase 1 budget and milestones")
    pdf.table(
        ["Work package", "Hours", "EUR"],
        [
            ["Lathe XZ stabilization", "35", "1,575"],
            ["Side Drill validation", "20", "900"],
            ["4th-axis example sanity", "15", "675"],
            ["CI / deb / pytest", "22", "990"],
            ["VALIDATION.md + release 2.0b-6", "12", "540"],
            ["Admin + reporting", "8", "360"],
            ["Contingency", "18", "810"],
            ["Total", "130", "6,000"],
        ],
        [100, 30, 30],
    )
    pdf.table(
        ["Milestone", "EUR", "Deliverable"],
        [
            ["M1 (30%)", "1,800", "CI green: Actions, pytest, .deb build"],
            ["M2 (40%)", "2,400", "Lathe XZ + Side Drill validated with tests"],
            ["M3 (30%)", "1,800", "VALIDATION.md, release 2.0b-6, 4th-axis sanity"],
        ],
        [30, 25, 105],
    )

    pdf.section_title("3. Four-phase roadmap (future - not Phase 1 contract)")
    pdf.table(
        ["Phase", "Amount", "Weeks", "Scope", "Submit"],
        [
            ["1 (this)", "EUR 6,000", "4", "Stabilize baseline, CI, docs", "Nov 2026"],
            ["2", "EUR 13,000", "8", "Operation IR + dual post + 4th axis", "May 2027"],
            ["3", "EUR 20,000", "10", "Siemens ISO subset, dual-output", "Nov 2027"],
            ["4", "EUR 26,000", "12", "5-axis indexing, i18n, packaging", "May 2028"],
            ["Total", "EUR ~65,000", "34", "Multi-controller open CAM", "-"],
        ],
        [22, 28, 18, 72, 28],
    )
    pdf.body_text(
        "Each phase is a separate NLnet proposal after public deliverables of the previous phase."
    )

    pdf.add_page()
    pdf.section_title("4. Architecture (future phases)")
    pdf.set_font("Courier", "", 9)
    arch = (
        "  Feature configs (.cfg)  -->  Operation IR (Ph.2)  -->  Post-processors\n"
        "  lathe/xz_profile.cfg         JSON/dataclasses          LinuxCncPost\n"
        "  mill/drill-side.cfg                                    IsoGenericPost (Ph.2)\n"
        "                                                         SiemensIsoPost (Ph.3)\n\n"
        "Phase 1 validates existing Feature -> NGC path only."
    )
    pdf.multi_cell(0, 5, arch)
    pdf.ln(6)

    pdf.section_title("5. Prior work and links")
    pdf.body_text(
        "- Lathe XZ profiles: G71/G72/G73 on devel - cfg/lathe/xz_profile.cfg, "
        "examples/lathe/xz_profile_demo.xml\n"
        "- Side Drill: cfg/mill/drill-side.cfg (horizontal spindle drilling)\n"
        "- Validation harness: PR #6 - scripts/validate_project.py, "
        ".github/workflows/validate.yml, 40+ pytest tests\n"
        "- 4th axis demo: examples/mill/4th-axis.xml\n"
        "- License: GPL. Platform: Debian 13, LinuxCNC 2.9+"
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print("Wrote %s" % OUT)


if __name__ == "__main__":
    main()
