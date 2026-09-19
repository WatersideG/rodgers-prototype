---
name: waterside-web-build
description: The build standard for any website, page, template, component, or redesign for Waterside Group and its brands on the Next.js / Vercel / Payload CMS stack. Use this whenever the task involves designing or building a web page or site, choosing typography, color, grid, spacing or motion for the web, wireframing a page, writing page copy for search or AI visibility, reviewing an existing site, or setting performance budgets. Use it even when the request is casual ("make a landing page", "mock up the services page", "fix this hero") and even when no brand is named. Do not fall back on generic web-design defaults for Waterside work.
---

# Waterside Web Build Standard

This skill governs how a Waterside site gets designed and built. It exists because the
default output of an AI assistant is competent and anonymous, and anonymous is the one
thing this work cannot be.

Version 1.0 · September 2026 · Owner: Mike Ciolino, CMO
Stack scope: Next.js (App Router) · Vercel · Payload CMS 3.x · Tailwind

## Provenance tags

Every rule in the reference files carries one of three tags. They are not decoration.
Treat them differently.

- `[documented]` — written in a Waterside governing document. Binding. Do not deviate
  without saying so out loud.
- `[measured]` — extracted from a shipped Waterside site. Describes what exists, not
  necessarily what should. Follow it unless a `[documented]` rule conflicts, and flag
  the conflict.
- `[open]` — not yet decided. Do not invent an answer. Ask, or state the assumption
  in plain language at the top of the work so it can be corrected.

An untagged claim in this skill is an error. Report it rather than acting on it.

## Before anything gets built

Five decisions gate the work. Nothing is drawn, coded, or wireframed until each one
has an answer from Mike or an explicit recorded assumption.

1. **Type system.** Families, fluid scale, the fixed steps, letter-spacing set.
   See `references/open-decisions.md` — this is currently contested between the
   documented standard and the shipped Longfellow site.
2. **Palette.** Which named values, and whether it derives from Radix Colors or is
   hand-chosen.
3. **Grid and containers.** Breakpoints and max-widths, and whether the Tailwind
   defaults count as a decision or as leftovers.
4. **Motion.** Duration range and easing, plus the reduced-motion behavior.
5. **Image treatment.** Crop ratios, density, and whether photography carries the page
   or supports it.

If the answer to any of these is "use your judgment," say which default you are taking
and why, in one sentence, before proceeding.

## Reference map

Read the file you need. Do not read all of them by habit.

| File | Read it when |
| --- | --- |
| `references/design-standard.md` | Any visual decision: type, color, spacing, motion, composition, page rhythm |
| `references/patterns.md` | Choosing a UI pattern: headers, nav, footers, galleries, forms, sticky elements, search and sort |
| `references/seo-aio.md` | Writing page copy, headings, schema, metadata, or anything aimed at search or AI citation |
| `references/performance.md` | Budgets, third-party scripts, image and font handling, launch verification |
| `references/sources-and-refresh.md` | Checking whether a rule is current, or running the weekly refresh |
| `references/open-decisions.md` | Any time a rule is tagged `[open]` |

## Rules that always apply

These hold on every Waterside web surface regardless of brand or page type.

- Never Arial. `[documented]`
- No table borders or table box rules in user-facing content. `[documented]`
- No clichés, no corporate filler, no AI-sounding copy. The banned phrase list in
  `references/design-standard.md` is not exhaustive; the test is whether a sentence
  could appear on any competitor's site unchanged. `[documented]`
- WCAG 2.2 AA is the floor, not the target. Accessibility failures block merge.
  `[documented]`
- Server-rendered HTML for anything that needs to be found. AI crawlers do not execute
  JavaScript, so a client-rendered page is invisible to them regardless of quality.
  `[documented]`
- Core Web Vitals are measured in the field at the 75th percentile of real users. A
  Lighthouse 100 on a developer machine is not evidence. `[documented]`
- Alt text is required at upload, not at use. `[documented]`

## What this skill does not do

It does not replace the governing documents. The SEO & AIO Developer Checklist governs
what gets done; the Payload SEO Integration Spec governs how; Dev Foundations Part I
governs process, security, accessibility and budget. This skill carries the design
judgment those documents leave undefined, and points at them for everything else.

Where this skill conflicts with the Checklist or Dev Foundations, those documents win.
Report the conflict rather than quietly resolving it.
