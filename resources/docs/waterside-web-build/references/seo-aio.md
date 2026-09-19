# SEO and AIO

Three documents govern this area. This file does not restate them. It points at them
and carries the rules that bear directly on design and copy decisions.

| Document | What it governs |
| --- | --- |
| SEO & AIO Developer Checklist (v1.0, May 2026) | The what. 22 categories, every item P0/P1/P2 with a verification method. |
| Payload SEO Integration Spec (v1.0, May 2026) | The how, on Payload 3.x and Next.js App Router. |
| SEO + AIO Strategy & Content Worksheet | The per-project fill-in. Complete at kickoff, revisit quarterly. |
| AIO Research Brief (May 2026) | The evidence behind all three. |

Where the Spec and the Checklist disagree, the Checklist governs the what and the Spec
governs the how. `[documented]`

## Rules that shape the page itself

From the AIO Research Brief. These change how copy gets written and how a template is
structured, which is why they live here rather than only in the Checklist.

`[documented]`:

- **Direct answer first.** Every section opens with 40 to 75 words answering a real
  question. Passages in that band were cited 3.1x more often than longer ones.
- **Question-format headings.** H2s and H3s phrased as questions were roughly 3.4x more
  likely to be extracted than topic-only headings.
- **Front-load.** 44.2% of citations come from the first 30% of the content.
- **Statistics with attribution.** Adding specific, sourced statistics lifted citation
  rates 30 to 40%. Vague claims get skipped.
- **Pronoun specificity.** Name the entity instead of "it" or "this." Extraction strips
  context.
- **Freshness on a 13-week cadence,** with roughly 20% substantive revision. Date-only
  changes do not work and can trigger spam signals.
- **Server-side rendering is mandatory for discoverability.** Major AI crawlers do not
  execute JavaScript. Verify with `curl -s yoursite.com | grep og:title`.
- **Comparison and list formats** get cited disproportionately.

## Things the brief rates lower than the industry does

Useful for not over-investing:

- llms.txt: no major AI company has publicly committed to reading it. Low cost, no
  documented harm, no documented benefit. Implement if convenient; do not reprioritize
  content work around it. `[documented]`
- Schema: a signal amplifier, not a silver bullet. Studies disagree on the correlation.
  Implement Organization, Article or BlogPosting with `dateModified`, FAQPage,
  Service or Product, and LocalBusiness. JSON-LD only. Google deprecated HowTo in
  February 2026. `[documented]`
- Backlinks: brand mentions correlate roughly 3x more strongly with AI visibility than
  backlinks do. `[documented]`

## Two failure modes that cause silent invisibility

- **CDN-level crawler blocking.** Cloudflare's Bot Fight Mode blocks GPTBot,
  ClaudeBot, PerplexityBot and Google-Extended before requests reach origin. Server
  logs will not show it because the requests never arrive. Check this on every site.
  `[documented]`
- **The two-crawler model.** Blocking GPTBot does not block OAI-SearchBot. Sites that
  opted out of AI training have often blocked their own visibility in ChatGPT Search.
  Anthropic mirrors this with ClaudeBot, Claude-User and Claude-SearchBot. Google's
  Google-Extended controls Gemini training only and does not affect AI Overviews.
  `[documented]`

## Currency warning

The AIO brief sets its own next review for August 2026 and states that the field moves
on a quarterly cadence. As of September 2026 that review is overdue. Treat the brief's
specific statistics as needing verification before external use. The weekly refresh
task in `sources-and-refresh.md` handles this.
