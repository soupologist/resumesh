# resumesh

A personal resume generation system. All career data lives in one place; an agent reads a job description and produces a tailored `resume.pdf` from it.

## How it works

1. **Data** — internships, projects, and extracurriculars are stored as structured Markdown files under `data/`. Each file has YAML frontmatter (title, skills, tags, dates) and bullet points describing the work.

2. **Template** — `resume.tex` is the base LaTeX resume template. It is not edited by hand after initial setup.

3. **Agent** — given a job description, the agent reads all data files, selects the most relevant experiences, rewrites bullets to match the role, and generates a populated `resume.tex`. The LaTeX is then compiled to `resume.pdf`.

## Data structure

```
data/
├── internships/       # work experience entries
├── projects/          # personal and academic projects
└── extracurriculars/  # clubs, music, other activities
```

Each entry is a `.md` file with this shape:

```markdown
---
title: Role Title
company: Company Name      # or project name
location: City, Country
start: YYYY-MM
end: YYYY-MM               # or "present"

skills:
  - Python
  - FastAPI

tags:
  - backend
  - ai
---

Bullet point one describing impact.

Bullet point two describing impact.
```

## Usage

```bash
python generate.py --jd path/to/job_description.txt
```

Outputs `resume.pdf` in the project root.

## Stack

- **Data format:** YAML frontmatter + Markdown
- **Template:** LaTeX
- **Agent:** Claude (reads data + JD, selects and rewrites content, fills template)
- **Build:** `pdflatex`
