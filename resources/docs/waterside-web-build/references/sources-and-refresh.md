# Sources and Refresh

## Designated sources

### Research, tracked weekly

| Source | Access |
| --- | --- |
| Nielsen Norman Group — free reports and articles | Public. Paid reports are titles only. |
| Baymard Institute | Premium library is behind account sign-in. An automated task cannot read it. Public research summaries only; new premium items get flagged by title for Mike to pull. |
| Google Search Central blog and Search Essentials | Public |
| web.dev and the Core Web Vitals project | Public |
| Schema.org | Public |
| Yoast SEO blog and site structure guide | Public |

### Implementation, checked on release rather than weekly

shadcn/ui, Radix Primitives, Radix Colors, Radix Icons, Next.js, Payload, Tailwind,
`modern-web-guidance` npm package. These change on version releases. Weekly checking
produces noise. Verify the pinned versions when a release ships or before a new build
starts.

## The weekly refresh task

Set up in Cowork as a scheduled task. Scheduled tasks run remotely on their cadence,
have access to skills and connectors, and each run produces its own session.

Task prompt:

> Check the Waterside web build sources for material change since the last run.
>
> Read: Google Search Central blog, web.dev, the Core Web Vitals project, NN/g's free
> reports and articles index, Baymard's public research summaries, and the release
> notes for Next.js, Payload, Tailwind, shadcn/ui and Radix.
>
> Report only material change: a threshold that moved, guidance that was withdrawn or
> added, a deprecation, a breaking release, or a new research finding that contradicts
> something in the waterside-web-build skill. Ignore restatements and marketing posts.
>
> For each item: what changed, which reference file it affects, the source URL, and the
> date. List new Baymard premium items by title only, flagged for Mike to pull.
>
> Do not edit the skill files. Produce a changelog for review.

Two conditions on this, or it degrades:

1. The source list stays fixed. Free-range searching produces volume, not signal.
2. Mike reviews the changelog before edits are applied. An unreviewed self-updating
   standard drifts within a quarter.

## Standing currency issues

- **AIO Research Brief** sets its next review for August 2026. Overdue as of September
  2026. This is the first job for the refresh task, not a new document.
- **Dev Foundations Part I** says 23 Waterside brands. The current count is 28.
- **Dev Foundations** flags its own open questions for quarterly revisit: which AI
  coding tool dominates, whether Visual Stability Index 2.0 becomes a formal Core Web
  Vital, AI's net effect on DORA metrics, and platform-specific AI citation tactics.

## Version log

| Date | Change |
| --- | --- |
| 2026-09-19 | v1.0. Built from Dev Foundations Part I, SEO & AIO Developer Checklist, Payload SEO Integration Spec, SEO+AIO Strategy Worksheet, AIO Research Brief, Flying Bridge UI & UX Research Report, and CSS extraction from longfellowdb.com. |
