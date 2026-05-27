# Trade2Swing — Deploy Guide (Cloudflare Pages)

This site is plain, static HTML/CSS — no build step, no framework. That makes it
fast, cheap, and portable. Below is everything needed to put it live on
`trade2swing.com`.

---

## 1. What's in this folder

```
trade2swing/
├── index.html               ← Landing page
├── weekly-earnings.html      ← Weekly Earnings Summary page
├── market-summary.html       ← Placeholder ("Coming soon")
├── watch-ready-lists.html    ← Placeholder ("Coming soon")
├── model-book.html           ← Placeholder ("Coming soon")
├── 404.html                  ← Friendly not-found page (Cloudflare uses this automatically)
├── assets/
│   ├── styles.css            ← Shared stylesheet for every page
│   ├── site.js               ← Tiny script (mobile menu only)
│   └── favicon.svg           ← Working favicon / logo mark
├── dashboard/
│   └── weekly-earnings-dashboard.html   ← The embedded dashboard (self-contained)
├── CONTENT-SPEC.md           ← Copywriting + structure + design reference (not published)
└── DEPLOY.md                 ← This file (not published)
```

The whole folder *is* the website. Everything in it gets served as-is.
`CONTENT-SPEC.md` and `DEPLOY.md` are reference docs — harmless if uploaded, but
you can leave them out of the published site if you prefer.

---

## 2. Favicon

Your favicon folder is already wired in. The site root contains:

```
favicon.ico
favicon-16x16.png
favicon-32x32.png
apple-touch-icon.png
android-chrome-192x192.png
android-chrome-512x512.png
site.webmanifest          (branded for Trade2Swing — theme color #6366f1)
```

Every page references the full set in its `<head>`, plus `assets/favicon.svg`
as a scalable fallback. No further action needed — when you replace your icon
files later, just overwrite them in place and redeploy.

---

## 3. Deploy — Option A: GitHub + Cloudflare Pages (recommended)

This gives you automatic re-deploys every time you push a change.

1. **Create a GitHub repo** (e.g. `trade2swing-site`) and upload the contents of
   this folder to it. GitHub Desktop or the web "upload files" button both work
   — no command line needed.
2. Go to **Cloudflare Dashboard → Workers & Pages → Create → Pages → Connect to Git**.
3. Pick your repo and click **Begin setup**.
4. **Build settings** — this is the important part:
   - Framework preset: **None**
   - Build command: **leave blank**
   - Build output directory: **`/`**  (just a slash — the files are at the root)
5. Click **Save and Deploy**. In under a minute you'll get a
   `your-project.pages.dev` URL.

## 3. Deploy — Option B: Direct upload (no GitHub)

1. **Cloudflare Dashboard → Workers & Pages → Create → Pages → Upload assets**.
2. Drag this whole folder in, name the project, and deploy.
3. To update later, repeat the upload. (Option A is nicer long-term because
   updates are automatic.)

---

## 4. Connect the domain `trade2swing.com`

1. In your new Pages project: **Custom domains → Set up a custom domain**.
2. Enter `trade2swing.com` (and add `www.trade2swing.com` too if you want).
3. If the domain's DNS is already on Cloudflare, the records are added for you.
   If not, Cloudflare will show the DNS records to add at your registrar.
4. HTTPS is issued automatically — no extra step.

---

## 5. Updating the Weekly Earnings dashboard each week

The dashboard is a single self-contained file:
`dashboard/weekly-earnings-dashboard.html`.

When your weekly earnings analysis produces a fresh
`Weekly_Earnings_Dashboard.html`, simply **overwrite that one file** (rename it to
`weekly-earnings-dashboard.html`) and re-deploy. Nothing else changes — the
`weekly-earnings.html` page embeds whatever is in that file. With Option A, that
means: replace the file in GitHub, and the live site updates on its own.

---

## 6. Testing locally before deploy

Because pages link with absolute paths (`/assets/styles.css`), open the site
through a tiny local server rather than double-clicking the file:

```
cd trade2swing
python -m http.server 8080
```

Then visit `http://localhost:8080`. (Opening `index.html` directly with
`file://` will not load the CSS — that's expected and only a local quirk; it
works fine once deployed.)

---

## Notes

- No cookies, no tracking, no browser storage — the site is fully static.
- The dashboard loads small company-logo images from Google's favicon service
  and links to your Substack; both need a normal internet connection.
- To add analytics later, Cloudflare Pages has free **Web Analytics** you can
  switch on in the project settings — no code change required.
