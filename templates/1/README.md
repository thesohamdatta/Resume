# Canonical resume template

`resume.cls` centralizes the approved Lato layout and shared resume macros. Its visual settings
are preserved from the former v3 class; the change consolidates the class interface and moves
its active path, rather than introducing a new visual design.

Mode content is authored in `versions/{mode}/_base.md` and rendered into TeX by
`pipeline/render_mode.py`. Application runs use the same class while tailoring content to their
input. Keep the template single-column, text-selectable, and one page; any proposed layout change
needs rendered and parsing evidence first.
