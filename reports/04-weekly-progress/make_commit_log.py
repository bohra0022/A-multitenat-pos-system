#!/usr/bin/env python3
"""Build the commit logs from git history.
Run from the repository root:  python3 reports/04-weekly-progress/make_commit_log.py
Writes (in reports/04-weekly-progress/):
  commit_log.csv          every commit
  commits_per_day.csv     commits per day and author
  frontend_work_log.csv   frontend commits with member and module
  frontend_summary.csv    frontend commits per member and module
"""
import csv, re, subprocess, collections, os

OUT = os.path.join("reports", "04-weekly-progress")
MEMBER = {  # git author name -> (full name, GitHub user)
    "bohra0022": ("Vrushay Bohra", "bohra0022"),
    "subhash8729": ("Subhash Dhaka", "subhash8729"),
    "Subhash Dhaka": ("Subhash Dhaka", "subhash8729"),
    "iamvkb7": ("Vimal Kumar", "iamvkb7"),
    "choubisavishvas-web": ("Vishvas Choubisa", "choubisavishvas-web"),
    "tanyasingh077": ("Tanya Singh", "tanyasingh077"),
}
ROLE = {
    "Vrushay Bohra": "Redux Toolkit part 1, Super Admin, testing and reports",
    "Subhash Dhaka": "Repository setup, Redux Toolkit part 2, Super Admin",
    "Vimal Kumar": "Cashier module",
    "Vishvas Choubisa": "Branch Manager module",
    "Tanya Singh": "Store module and onboarding",
}
AREA = {"pos-backend": "Backend", "pos-frontend-vite": "Frontend", "reports": "Reports"}
FE = "pos-frontend-vite/src/"
MODULES = [  # (path prefix, module), checked in order, compared in lower case
    (FE + "pages/superadmindashboard", "Super Admin"),
    (FE + "pages/store", "Store"),
    (FE + "pages/branch manager", "Branch Manager"),
    (FE + "pages/cashier", "Cashier"),
    (FE + "pages/onboarding", "Auth and onboarding"),
    (FE + "pages/common", "Auth and onboarding"),
    (FE + "pages/auth", "Auth and onboarding"),
    (FE + "redux toolkit", "Redux Toolkit"),
    (FE + "routes", "Routing"),
]

def module_of(path):
    p = path.lower()
    for prefix, name in MODULES:
        if p.startswith(prefix):
            return name
    return "Setup and shared"

raw = subprocess.run(
    ["git", "log", "--reverse", "--date=short", "--name-only",
     "--format=%x1e%h%x1f%an%x1f%ad%x1f%s"],
    capture_output=True, text=True, check=True).stdout

rows, fe_rows, per_day = [], [], collections.Counter()
for rec in raw.split("\x1e")[1:]:
    head, *files = rec.strip("\n").split("\n")
    h, author, day, msg = head.split("\x1f", 3)
    msg = msg.strip()
    files = [f for f in files if f.strip()]
    name = MEMBER.get(author, (author, author))[0]
    m = re.match(r"^\s*(\w+)(\([^)]*\))?:", msg)
    typ = "merge" if msg.startswith("Merge") else (m.group(1).lower() if m else "other")
    tops = collections.Counter(AREA.get(f.split("/")[0], "Docs") for f in files)
    area = tops.most_common(1)[0][0] if tops else ("Merge" if typ == "merge" else "Other")
    rows.append([h, day, name, ROLE.get(name, ""), msg, typ, area, len(files), "; ".join(files[:3])])
    per_day[(day, name)] += 1
    fe_files = [f for f in files if f.startswith(FE) or f.startswith("pos-frontend-vite/")]
    if fe_files:
        mods = collections.Counter(module_of(f) for f in fe_files)
        fe_rows.append([h, day, name, MEMBER.get(author, (author, author))[1],
                        mods.most_common(1)[0][0], msg, len(fe_files)])

def write(name, header, data):
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f); w.writerow(header); w.writerows(data)

write("commit_log.csv",
      ["No", "Commit hash", "Date", "Author", "Team role", "Commit message", "Type", "Area",
       "Files changed", "Example files"],
      [[i] + r for i, r in enumerate(rows, 1)])
write("commits_per_day.csv", ["Date", "Author", "Commits"],
      [[d, a, n] for (d, a), n in sorted(per_day.items())])
write("frontend_work_log.csv",
      ["No", "Commit hash", "Date", "Member", "GitHub user", "Module", "Commit message", "Files changed"],
      [[i] + r for i, r in enumerate(fe_rows, 1)])
summ = collections.Counter((r[2], r[4]) for r in fe_rows)
write("frontend_summary.csv", ["Member", "Module", "Frontend commits"],
      [[m, mod, n] for (m, mod), n in sorted(summ.items())])

print(f"{len(rows)} commits written to {OUT}/commit_log.csv")
for a, n in collections.Counter(r[2] for r in rows).most_common():
    print(f"  {n:3d}  {a}")
print(f"{len(fe_rows)} frontend commits in {OUT}/frontend_work_log.csv")
for (m, mod), n in sorted(summ.items()):
    print(f"  {n:3d}  {m}: {mod}")
