#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
TEMPLATE = ROOT / "template.tex"
OUTPUT_TEX = ROOT / "resume.tex"


def load_data() -> str:
    sections = []
    for category_dir in sorted(DATA_DIR.iterdir()):
        if not category_dir.is_dir():
            continue
        entries = sorted(category_dir.glob("*.md"))
        if not entries:
            continue
        sections.append(f"## {category_dir.name.upper()}")
        for path in entries:
            post = frontmatter.load(path)
            meta = post.metadata
            header = meta.get("title", path.stem)
            if "company" in meta:
                header += f" at {meta['company']}"
            period = f"{meta.get('start', '')} – {meta.get('end', '')}"
            location = meta.get("location", "")
            skills = ", ".join(meta.get("skills", []))
            sections.append(f"### {header}")
            sections.append(f"Period: {period} | Location: {location}")
            if skills:
                sections.append(f"Skills: {skills}")
            if post.content.strip():
                sections.append(post.content.strip())
            sections.append("")
    return "\n".join(sections)


def generate_tex(data: str, jd: str | None) -> str:
    template = TEMPLATE.read_text(encoding="utf-8")
    jd_block = f"\n\n## JOB DESCRIPTION\n{jd}" if jd else ""
    tailoring = "Tailor the selection and wording of bullets to match the job description." if jd else "Include all data as-is for a general resume."

    prompt = f"""Fill in the LaTeX resume template below using the career data provided. {tailoring}

## CAREER DATA
{data}{jd_block}

## TEMPLATE
{template}

Rules:
- Output ONLY the complete LaTeX source — no markdown fences, no explanation
- Replace the commented-out placeholder sections (Experience, Projects, Technical Skills, Extracurricular Activities) with real content from the data above
- Keep all LaTeX commands, the preamble, and personal info (name, email, links) exactly as in the template
- Keep bullet points concise and impact-focused
- Derive the Technical Skills section from the skills listed across all data entries
- Ensure the output is valid, compilable LaTeX"""

    result = subprocess.run(
        ["claude", "--print"],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8",
        shell=True,
    )
    if result.returncode != 0:
        print(result.stderr)
        sys.exit(1)
    return result.stdout.strip()


def compile_pdf():
    result = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", OUTPUT_TEX.name],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("pdflatex failed:")
        print(result.stdout[-3000:])
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate a tailored resume PDF")
    parser.add_argument("--jd", type=Path, help="Path to a job description file (optional)")
    parser.add_argument("--no-compile", action="store_true", help="Skip pdflatex compilation")
    args = parser.parse_args()

    jd_text = args.jd.read_text(encoding="utf-8") if args.jd else None

    print("Loading data...")
    data = load_data()

    print("Generating LaTeX...")
    tex = generate_tex(data, jd_text)
    OUTPUT_TEX.write_text(tex, encoding="utf-8")
    print(f"Written → {OUTPUT_TEX.name}")

    if not args.no_compile:
        print("Compiling PDF...")
        compile_pdf()
        print("Done → resume.pdf")


if __name__ == "__main__":
    main()
