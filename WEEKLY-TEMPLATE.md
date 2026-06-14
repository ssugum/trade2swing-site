# Trade2Swing Weekly — Template + Sunday Workflow

The forever-template. Each Sunday, copy the post template below into Substack,
fill the slots, publish. The goal is **never miss a week** — depth varies,
presence does not.

---

## 1. The Sunday workflow — ~2-3 hours total

Time budget you committed to. The schedule has redundancy built in so that if
Sunday afternoon falls through, the Substack post still ships.

### Saturday evening — Data refresh (30 min)

- [ ] Update MarketPulse Google sheet with Friday's close
- [ ] Save SPY weekly + QQQ (or NASDAQ Composite) daily screenshots from
      TradingView, your standard layout
- [ ] Confirm Watch and Ready lists in TradingView reflect this week's view
      (or duplicate to new ones if last week's are stale)
- [ ] Note any IPOs from the past 30 days for the IPO Radar
- [ ] No writing yet — just data prep

### Sunday morning — Substack post (75 min)

- [ ] In Substack, duplicate last week's post as a new draft
- [ ] Update date in headline and intro
- [ ] Refresh Market read (2-3 paragraphs + the SPY/QQQ chart)
- [ ] Refresh Sector commentary (1 paragraph + sector ETF watchlist link)
- [ ] Replace Watch & Ready list URLs (always check — TradingView regenerates)
- [ ] Insert the week's Stock Idea / Model Book entry teaser + link
- [ ] Update Earnings link if relevant context this week
- [ ] Update IPO Radar with this week's screenshot if running it

### Sunday afternoon — One Model Book entry on trade2swing.com (60 min)

- [ ] Clone the most recent Model Book entry HTML as a starting template
- [ ] Rename: `/model-book-YYYY-MM-DD-TICKER-or-theme.html`
- [ ] Replace ticker, dates, narrative; keep the section structure
- [ ] Update the Model Book index card on `/model-book.html`
- [ ] Run the recurring PS git workflow: `cd`, `git add .`, `git commit -m ""`, `git push`

### Sunday evening — Ship (15 min)

- [ ] Final read-through of Substack draft
- [ ] Hit Publish on Substack
- [ ] Confirm trade2swing.com Cloudflare redeploy completed (check live URL)
- [ ] Done

### If something has to give

The hard rule: **never skip in silence.** If the full post isn't going to happen:

1. **Mini-post:** publish a 150-word note on the market regime + a single link
   to the most recent Model Book entry. Headline: `Quick read — week of [DATE].`
   The cadence stays alive.
2. **Cross-post a past entry:** if an older Model Book entry is relevant to
   this week's setup, repost the link with a 2-paragraph "why it matters now"
   intro. New readers, no new writing.
3. The Model Book entry is the most skippable part. Substack ships first.

---

## 2. Substack post template — paste this into a new draft each week

Copy from the divider below into Substack. Bracketed `[FILL IN:]` slots are
what changes weekly. Sections marked OPTIONAL can be removed if time is tight.

---

```markdown
# [MM-DD-YYYY] US Stock Market Weekly: [HEADLINE]

### [Subhead — one phrase capturing this week's theme]

---

## 🧭 Market read

[FILL IN: 2-3 paragraphs on market regime. Distribution day count, leadership
behavior, key indices, anything that turned on or off this week.]

*[Insert SPY weekly + QQQ daily — your standard TradingView layout]*

[FILL IN: 1-2 paragraphs on the takeaway — what changed in the read, what
action it allows or blocks.]

---

## 🏭 Sector leadership

[FILL IN: 1-2 paragraphs on which sectors are leading or lagging this week.]

**Top groups:** [SECTOR1, SECTOR2, SECTOR3]
**Lagging:** [SECTOR1, SECTOR2]

[FILL IN: Sector ETFs TradingView watchlist link]

---

## 🎯 Watch & Ready lists

**[Watch list — setting up, no trigger yet →](FILL IN URL)**
Bases forming, monitor only.

**[Ready list — at or near a pivot →](FILL IN URL)**
Subset of Watch. First to act on if the broad signal supports.

> Always do your due diligence. This is not a buy or sell recommendation.

---

## 📓 Portfolio review (OPTIONAL)

[FILL IN: 1-2 sentences on portfolio posture only — cash %, position vs swing
tilt, any liquidations/adds this week. Detail lives in the Journal PPT.]

**[Trade2Swing Journal →](FILL IN: link to your Google Slides journal)**

---

## 🔥 Stocks on the move (OPTIONAL)

[FILL IN: 2-3 daily charts of biggest gainers / most active that are NOT
extended — still buyable from a setup, not chasing.]

---

## 📚 Model Book — this week's lesson

[FILL IN: One stock. The setup pattern. Why it's interesting now. Daily chart.
A line on the buy point, the stop, the sell rule. Then link to the full
study on trade2swing.com.]

**[→ Full Model Book entry on trade2swing.com](FILL IN URL)**

---

## 📡 IPO Radar (OPTIONAL)

[FILL IN: 1-2 paragraphs on recent IPOs forming bases. Multi-chart image
from TradingView.]

**[IPO list tracker →](FILL IN URL)**

---

## 📅 Earnings to track this week

[FILL IN: 2-3 sentences on which earnings prints matter this week and why.]

**[→ Weekly Earnings Summary on trade2swing.com](https://trade2swing.com/weekly-earnings.html)**

---

### Subscribe

Free, and stays free for now. If this is useful, subscribe so I know it's
being read.

---

**Disclaimer:** This is not a buy or sell recommendation. All content on
Trade2Swing — including market summaries, watch lists, charts, earnings data,
and the Model Book — is published for educational and informational purposes
only. Trading and investing in stocks involves substantial risk, including the
possible loss of capital. Past performance and historical chart examples do
not guarantee future results. Always do your own research and consider
consulting a licensed financial advisor before making any investment decision.

**CAN SLIM® trademark.** CAN SLIM® is a registered trademark of Investor's
Business Daily, Inc. "CANSLIM" is used here as the common shorthand for the
same methodology. Trade2Swing is independent and not affiliated with IBD.
```

---

## 3. Section-by-section playbook

Quick reference for what each section should look like at full speed.

### 🧭 Market read
- 2-3 paragraphs max. Lead with the regime call: uptrend, under pressure, correction.
- Reference distribution-day count if relevant.
- Close with what this allows or blocks for the week.

### 🏭 Sector leadership
- 1-2 paragraphs. Name 3 leading groups, 1-2 laggards.
- TradingView shareable list of sector ETFs.

### 🎯 Watch & Ready
- ALWAYS update the URLs. TradingView regenerates lists weekly.
- Watch = setting up, not yet actionable.
- Ready = at or near a pivot, actionable if regime supports.

### 📓 Portfolio review (optional)
- Keep VERY short. Link to the Journal PPT for detail.
- Only post posture, never dollar values.

### 🔥 Stocks on the move (optional)
- 2-3 daily charts MAX.
- Quality filter: not extended, still buyable from a setup.
- Skip if time short.

### 📚 Model Book — THE CORE
- One stock or cohort per week. This is the WEEK'S TEACHING.
- Always link to the full study on trade2swing.com.
- Builds the site over time. Long-arc asset.

### 📡 IPO Radar (optional)
- Multi-chart image from TradingView.
- Link to your IPO watchlist.

### 📅 Earnings
- 2-3 sentences. Always link to the Weekly Earnings Dashboard.
- The dashboard does the heavy lifting; the post just frames the read.

---

## 4. Pre-publish checklist

- [ ] Date in headline and intro is current
- [ ] All TradingView URLs refreshed
- [ ] At least one Model Book link present
- [ ] Disclaimer block present at bottom
- [ ] CAN SLIM® attribution present
- [ ] Read through once for typos and voice
- [ ] Substack title sounds like a teaser, not a label
- [ ] Push trade2swing.com if any new entry shipped
- [ ] Hit publish

---

## 5. The Model Book queue — content you already have

Painful trades from earlier this year that become Model Book entries. Each
one is roughly 90 minutes of writing once you've done the chart selection.

| Week target | Entry topic                              | Lesson core |
|-------------|------------------------------------------|-------------|
| Week 2      | META / HOOD / PLTR round-trip pattern    | When a winning year becomes flat and what the chart was warning |
| Week 3      | SNDK swing-vs-position misclassification | Telling them apart, what misclassifying costs |
| Week 4      | A single-name profile from the queue     | TBD — pick what's relevant to the week's market |
| Week 5      | A single-name profile from the queue     | TBD |

After these four, the rhythm produces fresh entries from the live trading
week. The queue is a buffer, not the destination.

---

## 6. Long-arc — where this is going

Free Substack is the front door. The trade2swing.com Model Book is the
long-term asset. Roughly 6-12 months out, the Model Book becomes the basis
for a paid tier — likely "first 7 days free, then paid archive." Every Model
Book entry written now is a deposit into that future tier.

**Goal by year-end 2026:**
- 26 weekly Substack posts
- 26 Model Book entries on trade2swing.com
- A subscriber count high enough to make the paid flip worth doing

The math is the schedule. The schedule is the system. Never miss a Sunday.
