# Design Standard

Contents: 1. Documented aesthetic · 2. Measured tokens from longfellowdb.com ·
3. Banned language · 4. Composition rules · 5. Component library policy ·
6. Proposed constraints pending ruling

---

## 1. Documented aesthetic

From Waterside Dev Foundations Part I, section 1.3. These apply to any public-facing
surface and any marketing-facing deliverable.

- Editorial, magazine-style design. `[documented]`
- Serif typography for body and display where appropriate. `[documented]`
- Never Arial. `[documented]`
- No table borders or table box rules in user-facing content. `[documented]`
- No marketing clichés, no overused corporate phrases, no AI-sounding copy.
  `[documented]`
- For technical deliverables: clear, professional, direct prose. One or two em-dashes
  per document at most. No padding with adjectives. `[documented]`
- Brand standards documents maintained by Ben Pessin and Jenna Colantuoni are
  authoritative for design that ships to users. When in doubt, ask. `[documented]`

Note the conflict with section 2 below. The documented standard calls for serif; the
reference implementation ships a single sans family. This is unresolved. See
`open-decisions.md`.

---

## 2. Measured tokens from longfellowdb.com

Extracted from the live CSS bundles, September 2026. These describe the reference
implementation. They are a starting point for a new build, not a mandate, and several
values are Tailwind defaults rather than choices.

### Typography `[measured]`

- Single family: Josefin Sans, with `system-ui, sans-serif` fallback. No second family
  anywhere on the site.
- Fluid heading steps, three of them:
  - `clamp(1.75rem, 3vw, 2.5rem)`
  - `clamp(1.9rem, 2.8vw, 2.25rem)`
  - `clamp(1.1rem, 1.6vw, 1.5rem)`
- Fixed sizes in use: 0.75, 0.875, 1.25, 1.875, 3, 3.75rem.
- Letter-spacing values in use: 0, .01, .02, .025, .04, .08, .1, .14, .15, .18, .2,
  .22, .35em. Thirteen values is accumulation, not a scale. See `open-decisions.md`.

### Color `[measured]`

A deliberate named palette, not framework defaults.

| Token | Value |
| --- | --- |
| `--navy` | `#2c3c4c` |
| `--navy-hover` | `#1a2830` |
| `--navy-06 / 12 / 15 / 20` | `#2c3c4c` at 06%, 12%, 15%, 20% |
| `--burgundy` | `#8b1a1a` |
| `--burgundy-deep` | `#5a0d0e` |
| `--burgundy-hover` | `#6e1515` |
| `--surface-cream` | `#f8f6f1` |
| `--surface-soft` | `#f5f6f7` |
| `--surface-warm` | `#e8ecef` |
| `--surface-steel` | `#4f6374` |
| `--surface-grid` | `#e8eaec` |
| `--surface-loading` | `#ced3d8` |
| `--color-primary` | `#1a1a1a` |
| `--color-body` | `#2d2d2d` |
| `--color-muted` | `#5a5a5a` |
| `--color-tab-inactive` | `#63737f` |

Three text weights and six surface tones is a workable system. Carry the structure to a
new brand even when the hues change: one dark anchor, one accent, a cream or warm base,
and three text values rather than one.

### Motion `[measured]`

- Durations in use: .15s, .2s, .25s, .26s, .3s, .35s, .5s, .7s.
- Easing: `cubic-bezier(.4, 0, .2, 1)` predominantly, with `ease-out` and `ease-in-out`.
- `prefers-reduced-motion` is honored. Keep this. Most sites skip it and it is a WCAG
  concern as well as a craft one.

### Structure `[measured]`

- Breakpoints: 640, 768, 1024, 1280, 1536 (Tailwind stock), plus 1200, 2000, and one
  `screen and (min-width: 800px)`.
- Container max-widths: 640, 768, 1024, 1280, 1536px (Tailwind stock).

The stock values were inherited, not chosen. Whether they become the standard is
`[open]`.

---

## 3. Banned language

Not exhaustive. The working test: if the sentence could appear unchanged on a
competitor's site, cut it.

Explicitly banned `[documented]`:

- "sits at the intersection of" and every variant of the intersection construction
- "in today's fast-paced world"
- "leverage synergies"
- marketing clichés and corporate filler generally

Also avoid `[open]`, proposed:

- The labeled-sentence device that assigns a role to an element and then explains it
  ("The ceiling is the frame"). It manufactures significance.
- Alliterative or catch-phrase closings that read as generated. Close on the plain
  result instead.
- Template sameness across a set. When several descriptions are written together, each
  should read as its own piece rather than a filled-in form.

---

## 4. Composition rules

These govern how a page is assembled rather than how it looks up close.

`[documented]`, from the AIO research brief and the Checklist:

- Server-render anything that needs to be found.
- Every section opens with a direct answer of 40 to 75 words. Passages in that range
  were cited 3.1x more often than longer ones in a 10,000-citation analysis.
- Roughly 44% of AI citations come from the first 30% of a page. Front-load substance.
- Replace "it" and "this" with named entities. Extraction pulls passages out of
  context, so a pronoun loses its referent.

`[open]`, proposed and awaiting ruling:

- One image treatment per site. Crop ratio, density, and grade stay consistent from
  hero to thumbnail. Mixed treatments are the clearest tell of an assembled page.
- A page changes rhythm at least once. A stack of identical full-width sections at
  identical spacing reads as a template regardless of content quality.
- No section explains what it is. Labels like "Our Process" above a three-step
  graphic add nothing the graphic does not already say.
- Second columns are earned. A page goes to two columns when the content is genuinely
  parallel, not to fill width.
- Photography carries Waterside pages. Illustration, iconography and gradient fills are
  substitutes for photography and should be treated as such.

---

## 5. Component library policy

shadcn/ui and Radix Primitives are approved as implementation sources. They solve
accessible component behavior correctly, which is worth more than rebuilding it.

`[open]`, needs a line drawn: shadcn has a recognizable default appearance. Adopting its
behavior while overriding its surface is the intended use here. What must be overridden
before ship, and what may pass through, is not yet decided. Until it is, restyle every
adopted component against the project's own tokens and say in the handoff which
components came from the library.

Radix Colors is available as a palette system. Whether it governs new brand palettes or
stays a reference is `[open]`. Longfellow's palette is hand-chosen, not Radix-derived.

Radix Icons is approved as an icon source.

---

## 6. Proposed constraints pending ruling

Everything in this file tagged `[open]` was drafted for Mike to accept, cut, or rewrite.
None of it binds until he rules. When a build needs one of these answered and no ruling
exists, state the assumption in one sentence and proceed; do not present the assumption
as the standard.
