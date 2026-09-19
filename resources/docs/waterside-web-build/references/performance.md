# Performance

## The budget

From Dev Foundations Part I, section 8.5. Enforced in pull requests through Lighthouse
CI. Violations require a fix or an explicit waiver with reasoning. `[documented]`

| Metric | Budget | Google's "good" threshold |
| --- | --- | --- |
| LCP | under 2.0s | under 2.5s |
| INP | under 150ms | under 200ms |
| CLS | under 0.05 | under 0.1 |
| JavaScript shipped | under 200KB compressed | — |
| Total page weight | under 2MB | — |
| Build time | under 10 minutes | — |
| Deploy time | under 5 minutes | — |

Measured in the field at the 75th percentile of real users via CrUX, not in the lab.
`[documented]`

## On the straight-100s goal

A Lighthouse 100 across all four categories is achievable on this stack with
disciplined asset and font handling. It stops being achievable the moment third-party
script lands on the page. The Checklist states the position directly: Core Web Vitals
are field measurements, and a Lighthouse 100 on a developer's machine means nothing if
the field 75th percentile fails. Roughly 43% of sites currently fail INP.

So the standard is written as a budget and an admission list, not as a score target.
Treat the lab score as a regression alarm and CrUX as the result.

## Admission list for third-party code

Nothing enters a page without a named owner and a measured cost. Items below are
ranked by how much damage they do to INP and LCP.

`[documented]`, from the Integration Spec and Dev Foundations:

- **GTM**, one container per brand, loaded once in the root layout. Consent Mode v2
  default state set to denied before GTM loads.
- **GA4**, with critical conversions also sent server-side through the Measurement
  Protocol so consent denial and blockers do not lose them.
- **Sentry**, server and client, filtered so 404s do not alert.
- **HubSpot forms**: use the headless pattern. Build the form in Payload's form builder,
  submit to a Next.js API route, proxy to the HubSpot Forms API. Native embeds route
  around the styling and accessibility standards.

`[open]`, needs a ruling: chat widgets, hosted video, embedded maps, booking engines,
and review widgets. Each of these can cost the INP budget on its own. Until a policy
exists, any of them entering a page requires a measured before-and-after and a
one-line justification.

## Asset handling

`[documented]`:

- `next/image` and `next/font`. Static generation by default, ISR where content
  changes.
- Payload media sizes: thumb 400x400, card 768x512, feature 1280x720, hero 1920x1080,
  og 1200x630. WebP at quality 82.
- Filenames normalized to a slugified version of the alt text on upload. Editors paste
  `IMG_4421.jpg`; the system stores a descriptive, indexable filename.
- Alt text required at upload, minimum 4 characters, maximum 125. Empty string only
  for genuinely decorative images.

## Launch verification

From the Integration Spec, phase 5. `[documented]`

- Full SEO/AIO Developer Checklist run as launch verification.
- Screaming Frog crawl with the Googlebot Smartphone user agent.
- Schema validated through Google Rich Results Test on home, service, project, post
  and contact page types.
- Lighthouse CI passing thresholds on five priority routes.
- Sitemap submitted in Google Search Console and Bing Webmaster Tools.
- axe DevTools plus manual keyboard and screen reader passes. Automated tools catch 30
  to 40% of accessibility issues at most.
