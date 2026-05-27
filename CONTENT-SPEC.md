# Trade2Swing — Content & Structure Spec

A reference companion to the deployable site. Captures the copywriting, the
page structure, the design system, and the voice — so the site can grow without
drifting.

---

## 1. Voice & tone

Trade2Swing is a research journal, not a tip sheet. The copy throughout the
site holds to four principles:

- **Process over picks.** Talk about the method, not the trade idea. Never
  imply a stock should be bought or sold.
- **Credible, not hypey.** No "10x returns," no urgency, no "secrets." The
  reader is treated as an adult who can read a chart.
- **Plain English over jargon.** CANSLIM and momentum vocabulary are explained
  in passing; nothing assumes prior familiarity beyond a basic interest in
  stocks.
- **Calm authority.** Confident, measured sentences. Short paragraphs. The
  feel of an analyst's note, not a marketing email.

When in doubt, ask: *would William O'Neil have written this paragraph?*

---

## 2. Design system

The aesthetic is **modern fintech** — clean, premium, contemporary. Distinct
from the "Bloomberg terminal" dark look and from old-school navy-and-gold
finance branding.

### Color palette

| Role | Token | Hex |
|---|---|---|
| Page background (default) | `--bg` | `#ffffff` |
| Soft section background | `--bg-soft` | `#f6f5fb` |
| Deep section background | `--bg-dark` | `#0e0a1f` |
| Primary text | `--ink` | `#15112b` |
| Secondary text | `--ink-soft` | `#4a4660` |
| Muted text | `--ink-mute` | `#7b7790` |
| Primary brand | `--brand` | `#6366f1` (indigo) |
| Brand accent | `--brand-2` | `#8b5cf6` (violet) |
| Brand deep | `--brand-deep` | `#4f46e5` |
| "Up" / growth green | `--up` | `#10b981` |
| Down / loss | `--down` | `#ef4444` |
| Highlight (coming soon) | `--amber` | `#f59e0b` |

The signature gradient `--grad` (`#6366f1 → #8b5cf6 → #a855f7`) is reserved for
the hero headline accent, primary buttons, and key brand moments. Used
sparingly so it keeps its impact.

Growth-green (`--up`) is the "this is working" color — used for check marks,
the live-status pill, and any directional cue. It is the only signal of
sentiment in the palette.

### Typography

- **Headings:** Sora (500–800 weight) — a geometric sans with a slightly
  futuristic feel that reads as "modern fintech" without becoming generic.
- **Body:** Inter (400–600 weight) — neutral, highly legible at all sizes,
  pairs cleanly with Sora.
- **Numerals:** Inter with tabular figures inside data displays.
- Both load from Google Fonts; the `<link>` tag is already in each page head.

Headline scale uses `clamp()` for fluid sizing — the hero headline scales from
~34px on mobile to ~58px on desktop without breakpoints.

### Layout & spacing

- Maximum content width: **1140px**, centered.
- Section padding: **84px** vertical on desktop, **60px** on mobile.
- Border-radius scale: **18px** for cards and major surfaces, **12px** for
  smaller chips and panels, **999px** for pills/buttons.
- Shadows are deliberately soft — small ambient shadow on cards, a larger
  glow only under the primary button on the hero.
- One-pixel `#e8e7f1` borders carry the cleanness; heavy borders are avoided.

### Imagery

No stock photography. The site relies on:

- A geometric SVG mark (an ascending bar trio with a swing arrow) used as
  both the header logo and the favicon.
- Inline SVG icons in pillar/expectation sections, all in the same line-art
  style at 24px viewBox, brand-color stroke.
- The dashboard itself supplies the only "data visuals" on the site, embedded
  on the Weekly Earnings page.

---

## 3. Site map

```
/                          Landing page
/weekly-earnings.html      Weekly Earnings Summary (live, embeds dashboard)
/market-summary.html       Coming soon
/watch-ready-lists.html    Coming soon
/model-book.html           Coming soon
/dashboard/weekly-earnings-dashboard.html   The embedded dashboard
/404.html                  Friendly not-found
```

Top navigation appears on every page: brand logo (links home), four content
links, and a "Subscribe" button pointing to Substack. The footer is identical
across pages and carries the full disclaimer.

---

## 4. Landing page — section-by-section

### 4.1 Hero

- **Pill (small badge above headline):** *"Growth stocks · CANSLIM · Momentum
  swing trading"* — names the three pillars in one breath.
- **Headline:** *"Trade the market's **true leaders** — by rules, not by
  feel."* The phrase "true leaders" is the wordmark of the site (echoes the
  Model Book). "By rules, not by feel" sets the discipline frame.
- **Sub-headline:** *"Trade2Swing is a research journal for disciplined
  growth-stock trading. It blends CANSLIM principles with momentum-based
  swing and position trading — and shows the process behind finding leaders,
  timing entries, and managing the rare monster winner."*
- **Calls to action:**
  - Primary: **Read the journal on Substack** → Substack profile
  - Ghost: **See this week's Earnings Summary** → `/weekly-earnings.html`
- **Trust strip (three small stats):** "5-step · A repeatable process",
  "Weekly · Market, sectors & watch lists", "Model Book · A growing study of
  leaders". These are factual hooks — process, cadence, depth — not
  performance claims.
- **Visual treatment:** Dark indigo background with two soft purple radial
  glows and a subtle grid overlay that fades at the edges. No hero image.

### 4.2 The Trade2Swing approach (the five pillars)

Eyebrow: *"The Process"*. Headline: *"The Trade2Swing approach."* Lead:
*"Every decision runs through the same five checkpoints, in order. The
discipline is the edge — skip a step and it disappears."*

Each pillar is rendered as a card with a small icon, a STEP 0X marker, a
short title, a 2–3 sentence explainer, and a CANSLIM tag.

1. **Market direction first** *(CANSLIM · M)* — "Roughly three of every four
   stocks follow the general market. Before any single idea, the broad trend
   is read — uptrend, under pressure, or correction — because it decides
   whether even the best setup is worth taking."
2. **Earnings & sales growth** *(CANSLIM · C + A)* — "True leaders are funded
   by real business momentum — accelerating quarterly earnings and sales,
   strong annual growth, and expanding margins. Fundamentals are the fuel
   behind a durable move."
3. **Leadership & relative strength** *(CANSLIM · L + I)* — "The goal is to
   own the standout, not the sympathy play. Relative strength versus the
   market, clear group leadership, and growing institutional sponsorship
   separate leaders from laggards."
4. **Price & volume action** *(CANSLIM · N + S)* — "Charts tell you when.
   Sound bases, clean pivots, and breakouts confirmed by a surge in volume
   show real demand from large investors — not a thin, low-conviction move
   that fades."
5. **Risk management** *(Discipline overlay)* — "The first job is to survive.
   Predefined stops, sensible position sizing, and clear rules for trimming
   into strength protect capital — so the rare big winner actually counts."

A sixth tile closes the row: *"One checklist, every time."* It explains that
the order matters and that no step is optional — and it links to the *What
you'll find here* section.

### 4.3 Why rules beat instinct (dark band)

A dark contrast section sits between the pillars and the education block, to
break the rhythm and signal that this is the philosophical heart of the site.

- Headline: *"Why rules beat instinct."*
- Lead: *"Markets are built to test conviction. A written process is what
  keeps a bad week from becoming a bad year."*
- Left column — checklist of five principles:
  - **A repeatable process** — Trading the same setup the same way makes
    results something you can study and improve, not just experience.
  - **Emotion stays out of the seat** — Entry, stop, and exit are defined
    while the chart is calm, before real money and real fear are in the
    picture.
  - **Losses are cut small by design** — The largest accounts are not the
    ones that were always right. They are the ones that were never badly
    wrong.
  - **Winners are managed, not gripped** — Rules for trimming into strength
    and trailing stops turn a good trade into a kept gain.
  - **Capital is the scoreboard** — You cannot compound from a deep hole.
    Protecting the downside is what makes the upside matter.
- Right column — a single quote-style card with the three house rules:
  > *"Cut every loss while it is still small. Let the leaders run. The general
  > market always gets the final word."*

  Attributed as: *"The three rules that sit above every Trade2Swing
  decision."* (House principles, deliberately not attributed to a named
  individual.)

### 4.4 What every investor and trader should know

Eyebrow: *"For beginners & intermediates"*. Headline: *"What every investor
and trader should know."* Lead: *"Two readers, two starting points — built on
the same foundation."*

Two side-by-side cards.

**Just starting out** (green badge):
- A small number of true leaders drive most of the gains in any market cycle
  — index-average thinking quietly misses them.
- The general market's direction matters more than any single pick. Learn to
  tell an uptrend from a correction before anything else.
- A "base" is a stock resting and building a launch pad. Buying out of a
  sound base beats chasing one that has already run far.
- Never average down on a losing position. Cutting a loss near 7–8% is cheap
  insurance, not a personal failure.
- Decide your exit before you enter. A plan made under pressure is almost
  always the wrong one.

**Sharpening the edge** (indigo badge):
- Refine entries — tell a proper pivot and a confirming volume surge apart
  from a thin, low-conviction breakout.
- Manage winners deliberately: trim partial size into strength, trail stops,
  and respect key moving averages.
- Size positions to conviction and to the market regime — not to excitement.
  Treat every add-on as its own trade.
- Study history. Build a model book of past and present leaders so today's
  setup always has a reference.
- Track every trade — setup, entry, exit, and the lesson. The log is where
  real instinct gets built.

### 4.5 What you'll find here

Eyebrow: *"Weekly content"*. Headline: *"What you'll find here."* Lead:
*"Trade2Swing publishes on a weekly rhythm. Every piece is educational — a
look at process and market structure, never a tip sheet."*

A single stacked list. Each row carries an icon, a title, one-sentence
description, and a status pill (**Live** in green or **Coming soon** in
amber).

1. **Weekly Earnings Summary** *(Live)* — A data dashboard of upcoming
   earnings across ~50 stocks: sales and EPS growth, price versus the
   52-week high, volume, and catalysts. Data only, no opinions.
2. **Market Summary & Sector Strength** *(Coming soon)* — A weekly read on
   overall market direction and health, and which sectors are leading or
   lagging the move.
3. **Watch & Ready Lists** *(Coming soon)* — Leaders setting up (watch) and
   leaders at or near a buy point (ready), shared for study and observation,
   never as signals.
4. **The Model Book** *(Coming soon)* — A growing library of true market
   leaders, past and present, studied chart by chart to sharpen pattern
   recognition.
5. **Weekly Model Chart** *(Coming soon)* — One highlighted chart each week
   on the hardest skill in trading — managing a monster winner without
   giving the gain back.

### 4.6 Substack CTA band

A dark, rounded card the width of the page content. Eyebrow *"The weekly
journal"*, headline *"Read Trade2Swing on Substack"*, copy:
*"The full write-ups — market summaries, watch lists, and model-chart
breakdowns — are published to subscribers on Substack. This site will grow
into the home for all of it; for now, Substack is where the weekly
conversation lives."* Button: **Subscribe on Substack →**.

This sits above the footer and is the strongest conversion moment on the
page, matching the "Substack first, site is the future hub" positioning.

### 4.7 Footer

- Brand wordmark and blurb (left): *"A research journal on disciplined,
  rules-based growth-stock trading — CANSLIM principles paired with momentum
  swing and position trading. Building a Model Book of true market leaders,
  one week at a time."*
- **Explore** column (center): Home / Weekly Earnings Summary / Market
  Summary / Watch & Ready Lists / Model Book.
- **Connect** column (right): Substack profile · `trade2swing@gmail.com`.
- **Full disclaimer block:** Lead sentence in bold — *"This is not a buy or
  sell recommendation."* — followed by two short paragraphs covering
  educational-purpose-only, risk of loss, past performance, and the
  "consult a licensed advisor / do your own research" closer.
- Bottom strip: © 2026 Trade2Swing · trade2swing.com — Educational content
  only · contact link.

---

## 5. Weekly Earnings Summary page — structure

The page wraps the existing dashboard in clean chrome so it feels like a
proper section of the site, not a raw artifact.

1. **Top nav** — shared site nav; "Weekly Earnings Summary" link is marked
   active.
2. **Dark page header** with a breadcrumb (`Home / Weekly Earnings
   Summary`), the page title, and a one-paragraph description:
   *"A weekly equity-research dashboard tracking upcoming earnings reports
   across roughly 50 stocks — grouped by sector, with sales and EPS growth,
   price relative to the 52-week high, average volume, and the catalyst
   behind each name."*
3. **Intro + disclaimer strip** — a short framing paragraph and a soft
   "educational data, not a recommendation" notice with a shield icon. Sets
   expectations before the data appears.
4. **Embedded dashboard** — a card with a faux browser-bar header (three
   dots, title *"Weekly Earnings Dashboard"*, an "Open full dashboard ↗"
   link), and the dashboard rendered inside an iframe at full width. A
   fallback "Dashboard not displaying? Open it in a new tab" link sits
   directly underneath.
5. **How to read this** — a six-card grid explaining the KPI strip, hot
   sector themes, off-52-week-high column, sales & EPS growth, 50-day
   average volume, and the click-to-expand catalyst row.
6. **Process tie-back** — a small panel reminding readers that earnings are
   step two of the Trade2Swing approach: this dashboard surfaces *where the
   growth and catalysts are*; entry timing still depends on market
   direction, the chart, and a risk plan.
7. **Footer** — same shared footer with the full disclaimer.

**Weekly update flow:** the embedded file is
`/dashboard/weekly-earnings-dashboard.html`. Each week, overwrite that one
file with the freshly generated dashboard — the wrapping page picks the
update up automatically. No other change is needed.

---

## 6. Placeholder pages

The three coming-soon pages — Market Summary, Watch & Ready Lists, and Model
Book — share a single layout: shared nav, a centered block with an icon
glyph, a "Coming soon" tag, the page title, a one-paragraph description of
what will live there, a short preview list of what to expect, and two
buttons (subscribe on Substack as primary, back-to-home as secondary).
Footer is identical to other pages.

Replace each with full content when the underlying weekly workflow goes
live. The site map and nav already reserve their place.

---

## 7. Disclaimer — exact wording

The line that anchors the brand:

> **This is not a buy or sell recommendation.**

The longer educational disclaimer (used in the footer of every page):

> All content on Trade2Swing — including market summaries, watch lists,
> charts, earnings data, and the Model Book — is published for educational
> and informational purposes only. Nothing here is investment, financial,
> legal, or tax advice, an offer or solicitation to buy or sell any
> security, or a recommendation for any particular person.
>
> Trading and investing in stocks involves substantial risk, including the
> possible loss of capital. Past performance and historical chart examples
> do not guarantee future results. Always do your own research and consider
> consulting a licensed financial advisor before making any investment
> decision. You are solely responsible for your own decisions.

The Weekly Earnings page additionally carries a shorter inline notice on
data sourcing: figures come from public sources and analyst-consensus
estimates, and volume figures are approximate.

---

## 8. Where the site grows from here

A short evolution roadmap, in priority order:

1. **Light up Market Summary** — convert the placeholder into a real weekly
   page once the rhythm is established. The dashboard pattern (one
   self-contained file embedded in the wrapper page) is reusable here.
2. **Watch & Ready Lists** — same pattern, with a small table or card
   layout per name. Keep it study-only language.
3. **The Model Book** — the long arc. Probably a chart gallery or an
   index by setup type, drawing from `canslim-skill/model-book/` entries.
4. **Weekly Model Chart** — could live inside the Model Book page or as a
   pinned section on the landing page.
5. **Optional later:** an RSS feed cross-posted from Substack, a search box
   over the Model Book, and tasteful Cloudflare Web Analytics. None of
   these change the architecture of the site.

The point of starting plain and static is that none of these additions
break what is already shipped.
