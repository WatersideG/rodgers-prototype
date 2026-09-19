# Open Decisions

Everything here blocks a rule somewhere else in the skill. Until each is answered, the
affected rule stays `[open]` and any build that touches it must state its assumption
out loud rather than present it as the standard.

## 1. Typography: serif or Josefin Sans

Dev Foundations 1.3 specifies serif typography for body and display where appropriate,
and names Brown and Miller Banner as the Longfellow brand fonts. The shipped
longfellowdb.com uses Josefin Sans alone, a sans, with no second family.

One of these is the standard. Which one, and does the answer apply portfolio-wide or
per brand?

Affects: `design-standard.md` sections 1 and 2.

## 2. Tailwind defaults: decision or residue

Breakpoints at 640, 768, 1024, 1280, 1536 and the matching container max-widths are
Tailwind stock. Transition durations of .15s, .2s and .3s are also Tailwind stock. The
1200, 2000 and 800px stops are deliberate.

Do the stock values become the standard, or does a specified set replace them so the
next build has to hit them deliberately?

Affects: `design-standard.md` section 2, and gate 3 in SKILL.md.

## 3. Letter-spacing scale

Thirteen distinct values ship on Longfellow, from 0 to .35em. That is accumulation.
Fix a scale, or leave it open to the designer?

Affects: `design-standard.md` section 2.

## 4. Radix Colors

Radix Colors provides 12-step scales with paired light, dark and alpha ramps.
Longfellow's palette is hand-chosen: one navy, one burgundy, six surfaces, three text
values.

Does Radix Colors become the method for generating new brand palettes, or stay a
reference while palettes are chosen by hand?

Affects: `design-standard.md` section 5, and gate 2 in SKILL.md.

## 5. shadcn override line

What must be overridden before a shadcn component ships, and what may pass through as
delivered? The library solves accessible behavior correctly and carries a recognizable
default appearance.

Affects: `design-standard.md` section 5.

## 6. Flying Bridge research scope

Generalize the 274-source report into the portfolio-wide pattern standard every build
works from, or keep it a brand reference the skill cites for specific patterns?

Affects: `patterns.md`.

## 7. Third-party admission policy

Chat widgets, hosted video, embedded maps, booking engines and review widgets each
threaten the INP budget. A standing policy on what is admitted, under what conditions,
and with what measured cost.

Affects: `performance.md`.

## 8. Enforcement scope

Does this standard govern only sites Mike personally directs, or everything the
Northeastern co-op teams ship on the platform? The answer determines how much is
written as a hard gate versus guidance.

Affects: the whole skill.

## 9. The rejection list

The proposed constraints in `design-standard.md` sections 3, 4 and 5 were drafted for
review, not derived from a ruling. The more useful half, still missing: specific sites
or patterns Mike considers machine-made, in his words. That list does more work than the
positive examples.

Affects: `design-standard.md` sections 3 and 4.
