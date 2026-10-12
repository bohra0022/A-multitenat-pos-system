#!/usr/bin/env python3
"""Update only the Weekly Plan and Team sections of README.md.
Run from the repository root:  python3 reports/04-weekly-progress/update_readme_plan.py
Other parts of the README are left untouched.
"""
import re
P = "reports/04-weekly-progress/readme_sections.md"
txt = open(P, encoding="utf-8").read()
plan = txt.split("<!-- PLAN -->")[1].split("<!-- TEAM -->")[0].strip("\n")
team = txt.split("<!-- TEAM -->")[1].strip("\n")
readme = open("README.md", encoding="utf-8").read()

m = re.search(r"## 📅 Weekly Plan.*?(?=\n---\n)", readme, flags=re.S)
if m:
    readme = readme[:m.start()] + plan + "\n" + readme[m.end():]
    print("Weekly Plan section replaced")
else:
    first = readme.index("\n") + 1
    readme = readme[:first] + "\n---\n\n" + plan + "\n\n---\n" + readme[first:]
    print("Weekly Plan section added after the title")

m = re.search(r"^## (?:👥 )?Team( and frontend modules)?[ \t]*\n.*?(?=\n## |\Z)", readme, flags=re.S | re.M)
if m:
    readme = readme[:m.start()] + team + "\n" + readme[m.end():]
    print("Team section replaced")
else:
    readme = readme.rstrip("\n") + "\n\n" + team
    print("Team section added at the end")
open("README.md", "w", encoding="utf-8").write(readme + ("\n" if not readme.endswith("\n") else ""))
