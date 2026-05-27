# Git workflow - Trade2Swing site

A quick-reference for pushing changes from your local folder to GitHub
(and through to the live site on Cloudflare Pages). Written for
PowerShell on Windows.

---

## Your setup at a glance

- Project folder: `C:\Users\ssugu\OneDrive\Importantdocs\Claude\Projects\trade2swing`
- GitHub repo: `https://github.com/ssugum/trade2swing-site`
- Branch: `main`
- Hosting: Cloudflare Pages (auto-deploys roughly 30-60 seconds after each push)

---

## The recurring routine

Every time you change something and want it live, run these five lines
in order:

```powershell
cd C:\Users\ssugu\OneDrive\Importantdocs\Claude\Projects\trade2swing
git status
git add .
git commit -m "Short description of what changed"
git push
```

That's the whole loop. After a few rounds it becomes muscle memory.

### What each line does

- **`cd ...`** - "change directory." Moves PowerShell into the project
  folder. Every git command runs against whatever folder you are in,
  so start here every time.
- **`git status`** - shows what has changed since the last commit. Always
  run this first so you know what you are about to ship. If it says
  "nothing to commit, working tree clean," there is nothing new to push.
- **`git add .`** - "stages" your changes - meaning, marks them as ready
  for the next commit. The `.` means "everything in this folder."
- **`git commit -m "..."`** - bundles the staged changes into one labeled
  snapshot. Write a short, present-tense message describing what you did.
  Good: `"Update homepage hero copy"`. Less good: `"changes"`.
- **`git push`** - sends the commit up to GitHub. Cloudflare sees the new
  commit within a minute and rebuilds the site automatically.

---

## Useful one-off commands

## git --version
## git config --global user.name "ssugum"
## git config --global user.email "ssugum@gmail.com"
- `git log --oneline -10` - show the last 10 commits as one-line summaries.
- `git diff` - show exactly which lines changed in your modified files.
- `git diff --staged` - show what is already staged for the next commit.
- `git restore <filename>` - undo unstaged changes to a single file.
  Careful - this is unrecoverable.
- `git remote -v` - show which GitHub repo this folder is connected to.

---

## Common scenarios

### Updating the Weekly Earnings dashboard each week

When your scheduled task produces a fresh dashboard:

1. Copy the new `Weekly_Earnings_Dashboard.html` into
   `C:\...\trade2swing\dashboard\`.
2. Rename it to `weekly-earnings-dashboard.html`, overwriting the old one.
3. Run the recurring routine. A natural message:
   `git commit -m "Update Weekly Earnings dashboard for week of YYYY-MM-DD"`.

The page wrapper (`weekly-earnings.html`) doesn't need to change - it
just iframes whatever is in `dashboard/weekly-earnings-dashboard.html`.

### Editing copy on a page

1. Open the HTML file in any text editor (VS Code, Notepad, even WordPad).
2. Make your edits and save.
3. Run the recurring routine.

### Adding a brand-new page

1. Create a new HTML file in the project folder (copy an existing
   "coming soon" page as a starting template - the nav and footer are
   already wired up there).
2. Add a link to the new page inside the top-nav block of every page
   (look for `<ul class="nav-links">`).
3. Run the recurring routine.

### Editing the shared stylesheet

`assets/styles.css` controls the look of every page at once. Change a
color or spacing rule there and the change ripples through the whole
site after one commit + push.

---

## Common errors and what they mean

- **"Everything up-to-date"** on push - no new commits exist that aren't
  already on GitHub. Either you've already pushed, or `git add` plus
  `git commit` didn't actually run. Run `git status` to see.

- **"src refspec main does not match any"** - there is no commit on a
  branch called `main` to push. You probably ran `git push` before
  `git commit`. Run `git status` to confirm, then commit any pending
  changes before pushing.

- **"Updates were rejected because the remote contains work that you do
  not have locally"** - someone (or another machine, or you on the
  GitHub web UI) pushed something you don't have a copy of. Run
  `git pull` first to bring your local up to date, then `git push`.

- **"nothing to commit, working tree clean"** - you have no unsaved
  changes. Either you saved the wrong file, or the change was already
  committed earlier. Run `git log --oneline -5` to see recent commits.

- **Push prompts for a username and password** - this is normal on the
  first push from a new machine. Sign in through the browser window
  that pops up. Git Credential Manager remembers you after that.

---

## OneDrive caveats

This folder lives inside OneDrive, which is usually fine but can
occasionally fight with git:

1. **One-time fix:** right-click the `trade2swing` folder in File
   Explorer once and pick "Always keep on this device." This stops
   OneDrive from making files cloud-only and prevents most weirdness.
2. **If git acts strangely** (file locked, can't write, partial files):
   right-click the OneDrive cloud icon in the system tray, choose
   "Pause syncing" for 2 hours, do your git work, then let it resume.

---

## A note on good commit messages

A year from now, `git log --oneline` becomes your changelog. Write
messages your future self can scan in two seconds:

- Yes: `"Add weekly model chart for AMD"` / `"Fix typo in hero subhead"`
- Yes: `"Update earnings dashboard - week of 2026-06-01"`
- No: `"updates"` / `"final"` / `"asdf"` / `"."`

One commit per "thing you did" keeps the history clean and lets you roll
back precisely if something breaks.

---

## The 30-second version

If you only remember three things:

1. Start every session with `cd` into the project folder.
2. The push loop is always `git add . / git commit -m "..." / git push`.
3. Cloudflare deploys automatically about a minute after the push - no
   action needed on Cloudflare's side.

That's it. Welcome to the workflow.
