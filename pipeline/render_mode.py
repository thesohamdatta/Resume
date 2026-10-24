#!/usr/bin/env python3
"""Render the constrained mode-resume Markdown format into the shared LaTeX template."""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODES = {"startup", "mnc", "referral"}
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


def tex_text(value: str) -> str:
    """Convert the supported inline Markdown subset to safe LaTeX text."""
    links: list[str] = []

    def hold_link(match: re.Match[str]) -> str:
        links.append(r"\href{" + match.group(2) + "}{" + tex_text(match.group(1)) + "}")
        return f"@@LINK{len(links) - 1}@@"

    value = LINK_RE.sub(hold_link, value)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }
    value = "".join(replacements.get(char, char) for char in value)
    value = BOLD_RE.sub(lambda match: r"\textbf{" + match.group(1) + "}", value)
    for index, link in enumerate(links):
        value = value.replace(f"@@LINK{index}@@", link)
    return re.sub(r"\s*·\s*", " | ", value).replace("–", "--")


def parse_header(lines: list[str]) -> list[str]:
    nonempty = [line.strip() for line in lines if line.strip()]
    if len(nonempty) < 2 or not nonempty[0].startswith("# "):
        raise ValueError("expected name and contact line before the first section")
    name = nonempty[0][2:].strip()
    has_headline = len(nonempty) >= 3
    contact_line = nonempty[2] if has_headline else nonempty[1]
    headline = nonempty[1].strip("*").strip() if has_headline else ""
    links = list(LINK_RE.finditer(contact_line))
    plain_contact = LINK_RE.sub("", contact_line)
    parts = [part.strip() for part in re.split(r"\\s*·\\s*", plain_contact) if part.strip()]
    if not parts:
        raise ValueError("contact line must include a location")
    location = parts[0]
    details = [part for part in parts[1:] if "@" in part or re.search(r"\\+?\\d[\\d ()-]{6,}", part)]
    social = [r"\\href{" + match.group(2) + "}{" + tex_text(match.group(1)) + "}" for match in links]
    output = [
        r"\\resumeHeader{" + tex_text(name) + "}{" + tex_text(location) + "}{" 
        + r" | ".join(tex_text(item) for item in details) + "}{" 
        + r" | ".join(social) + "}",
    ]
    if has_headline:
        output.append(r"{\\small\\bfseries " + tex_text(headline) + r"}\\par\\vspace{2pt}")
    return output

def split_sections(lines: list[str]) -> tuple[list[str], list[tuple[str, list[str]]]]:
    header: list[str] = []
    sections: list[tuple[str, list[str]]] = []
    title: str | None = None
    body: list[str] = []
    for line in lines:
        if line.startswith("## "):
            if title is not None:
                sections.append((title, body))
            else:
                header = body
            title, body = line[3:].strip(), []
        elif title is None:
            body.append(line)
        else:
            body.append(line)
    if title is not None:
        sections.append((title, body))
    return header, sections


def blocks(lines: list[str]) -> list[tuple[str, list[str]]]:
    result: list[tuple[str, list[str]]] = []
    title: str | None = None
    body: list[str] = []
    for line in lines:
        if line.startswith("### "):
            if title is not None:
                result.append((title, body))
            title, body = line[4:].strip(), []
        elif title is None:
            if line.strip():
                raise ValueError(f"expected an entry heading, got: {line}")
        else:
            body.append(line)
    if title is not None:
        result.append((title, body))
    return result


def bullets(lines: list[str]) -> list[str]:
    output: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if not stripped.startswith("- "):
            raise ValueError(f"expected a bullet, got: {stripped}")
        output.append(r"\item " + tex_text(stripped[2:]))
    return output


def render_experience(lines: list[str]) -> list[str]:
    output: list[str] = []
    for heading, body in blocks(lines):
        if "·" not in heading:
            raise ValueError(f"experience heading must be 'Company · Role': {heading}")
        company, role = (part.strip() for part in heading.split("·", 1))
        metadata = next((line.strip() for line in body if line.strip()), "")
        if not metadata.startswith("**"):
            raise ValueError(f"experience entry needs a bold date line: {heading}")
        date_context = metadata.split("|", 1)
        dates = date_context[0]
        context = date_context[1] if len(date_context) > 1 else ""
        output.append(
            r"\resumeRole{" + tex_text(company) + "}{" + tex_text(role) + "}{"
            + tex_text(dates.strip().strip("*")) + "}{" + tex_text(context.strip()) + "}"
        )
        output.append(r"\begin{resumeitemize}")
        output.extend(bullets(body[body.index(next(line for line in body if line.strip())) + 1 :]))
        output.append(r"\end{resumeitemize}")
    return output


def render_projects(lines: list[str]) -> list[str]:
    output: list[str] = []
    for heading, body in blocks(lines):
        nonempty = [line.strip() for line in body if line.strip()]
        metadata: list[str] = []
        description: list[str] = []
        for line in nonempty:
            if line.startswith("- "):
                description.append(line)
            elif not description:
                metadata.append(line)
            else:
                raise ValueError(f"unexpected project line after bullets: {line}")
        links: list[str] = []
        technologies: list[str] = []
        for line in metadata:
            found = list(LINK_RE.finditer(line))
            links.extend(r"\href{" + match.group(2) + "}{" + tex_text(match.group(1)) + "}" for match in found)
            without_links = LINK_RE.sub("", line).strip(" ·").strip("*").strip()
            if without_links and without_links.lower() != "github":
                technologies.append(without_links)
        title = re.sub(r"\s*·\s*", ": ", heading)
        output.append(
            r"\resumeProject{" + tex_text(title) + "}{" + (links[0] if links else "")
            + "}{" + tex_text(" | ".join(technologies)) + "}"
        )
        output.append(r"\begin{resumeitemize}")
        output.extend(bullets(description))
        output.append(r"\end{resumeitemize}")
    return output


def render_education(lines: list[str]) -> list[str]:
    content = [line.strip() for line in lines if line.strip()]
    if len(content) < 2:
        raise ValueError("education needs degree and institution/date lines")
    degree = content[0].strip("*")
    institution_line = " ".join(content[1:])
    if "·" not in institution_line:
        raise ValueError("education institution line must end with '· dates'")
    institution, dates = (part.strip() for part in institution_line.rsplit("·", 1))
    return [r"\resumeEducation{" + tex_text(institution) + "}{" + tex_text(dates) + "}{" + tex_text(degree) + "}"]


def render_certifications(lines: list[str]) -> list[str]:
    """Render a compact set of linked credential names as a single ATS-readable paragraph."""
    names: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if not stripped.startswith("- "):
            raise ValueError(f"expected a certification bullet, got: {stripped}")
        names.append(stripped[2:])
    if not names:
        return []
    return [r"\tightpar{" + tex_text(" · ".join(names)) + "}"]


def render_skills(lines: list[str]) -> list[str]:
    output: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        match = re.fullmatch(r"\*\*(.+?):\*\*\s*(.+)", stripped)
        if not match:
            raise ValueError(f"skill line must be '**Label:** values': {stripped}")
        output.append(r"\resumeSkills{" + tex_text(match.group(1)) + ":}{" + tex_text(match.group(2)) + "}")
    return output


def render_mode(mode: str) -> str:
    source = ROOT / "versions" / mode / "_base.md"
    text = source.read_text(encoding="utf-8")
    header, sections = split_sections(text.splitlines())
    output = [
        "% Generated from _base.md by pipeline/render_mode.py. Edit the Markdown source.",
        r"\documentclass{../../templates/1/resume}",
        r"\begin{document}",
    ]
    output.extend(parse_header(header))
    for title, body in sections:
        if title == "Summary":
            output.append(r"\tightpar{" + tex_text(" ".join(line.strip() for line in body if line.strip())) + "}")
        elif title == "Experience":
            output.extend([r"\section{Experience}", *render_experience(body)])
        elif "Projects" in title:
            output.extend([r"\section{" + tex_text(title) + "}", *render_projects(body)])
        elif title == "Education":
            output.extend([r"\section{Education}", *render_education(body)])
        elif title == "Technical Skills":
            output.extend([r"\section{Technical Skills}", *render_skills(body)])
        elif title == "Certifications":
            output.extend([r"\section{Certifications}", *render_certifications(body)])
        else:
            raise ValueError(f"unsupported mode section: {title}")
    output.extend([r"\end{document}", ""])
    return "\n".join(output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=sorted(MODES))
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true", help="write the generated TeX file")
    action.add_argument("--check", action="store_true", help="fail if the generated TeX is stale")
    args = parser.parse_args()

    target = ROOT / "versions" / args.mode / "resume.tex"
    try:
        generated = render_mode(args.mode)
    except (OSError, ValueError) as error:
        print(f"FAIL: {args.mode}: {error}", file=sys.stderr)
        return 1

    if args.write:
        target.write_text(generated, encoding="utf-8", newline="\n")
        print(f"Wrote {target.relative_to(ROOT)}")
        return 0

    current = target.read_text(encoding="utf-8") if target.exists() else ""
    if current == generated:
        print(f"PASS: {args.mode} TeX matches _base.md")
        return 0
    print("".join(difflib.unified_diff(current.splitlines(keepends=True), generated.splitlines(keepends=True),
                                      fromfile=str(target.relative_to(ROOT)), tofile="generated from _base.md")),
          file=sys.stderr)
    print(f"FAIL: {args.mode} TeX is stale; run pipeline/render_mode.py {args.mode} --write", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
