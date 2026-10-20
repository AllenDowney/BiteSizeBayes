# BiteSizeBayes Project Board

Numbered tasks for tracking work. Each task has a permanent number; add new tasks at the end. Update status as work progresses.

**Status values:** `Pending`, `In progress`, `DONE`

---

## Task 1: Refresh

**Status:** In progress (2026-10-19)

**Context:** BiteSizeBayes is a "current" tutorial (GreenTeaPress Task 24), refreshed with the checklist in `~/GreenTeaPress/plans/workshops.md` ("Refresh checklist"); BayesMadeSimple was the pilot. It's a self-paced tutorial, not a workshop given live: no recordings (only a 4-minute lightning talk, NWDSE 2020). 136 stars; last content change 2021-03-29. The site (`allendowney.github.io/BiteSizeBayes/`) is a Jupyter Book 1 build from 2021, served from `gh-pages`.

**0. Set up**
- [x] `git fetch` / `pull` (one new commit, the README hub line); untracked files listed and decided (below), backed up to the session scratchpad
- [x] `PROJECT_BOARD.md` and `CLAUDE.md` (2026-10-19)
- [x] Tag `pre-refresh-2026` at `1e4e192` (pushed 2026-10-19). No recording tags
- [x] Inventory (below)
- [x] Env: `BiteSizeBayes` (Python 3.12.15, NumPy 2.5, pandas 3.0, SciPy 1.18, Matplotlib 3.11), created from a scratch spec; the repo's `environment.yml` is not yet rewritten

**1. Runs in a current environment**
- [ ] `environment.yml` (conda-forge, `python=3.12`, numpy, pandas, scipy, matplotlib, seaborn, sympy for monty, jupyter, pytest, nbmake, site build tools); drop `empiricaldist` (not imported anywhere) and `pytables` (only if `clean_gss_bayes` stops reading HDF5)
- [ ] `requirements.txt`, `requirements-dev.txt`
- [ ] First code cell: the notebooks already download `utils.py` and their data; check that nothing else is missing on Colab
- [ ] Fix breakage and deprecation warnings (list below)
- [ ] `http://` raw URL for `showcases.2012.csv` in `13_price` → `https://`
- [ ] README install section: Colab first, then pip or mamba (the README has no install section; drop the NBViewer links?)

**2. Tests and CI**
- [ ] `pytest --nbmake` on `solutions/*.ipynb`; student versions with `____` blanks (e.g. `bandit.ipynb`) need `raises-exception` tags or are left out
- [ ] `.github/workflows/tests.yml`, badge; replace `solutions/test.sh`

**3. Colab**
- [ ] "Click here to run this notebook on Colab" cell after the title of each notebook (solutions also link to the version with blanks); Colab links in the README table
- [ ] Allen runs one notebook on Colab end to end

**4. Text**
- [ ] Typos, docstrings, links (codespell plus reading the markdown)

**5. README in the standard shape**
- [ ] Rewrite (abstract, level, length, outline, notebook table with Colab links for exercises and solutions, running instructions, next steps, license)

**6. Site and visibility**
- [ ] Bring `jb/` up to the BayesMadeSimple template (`index.md`, `prep_notebooks.py` that copies the solutions, writes descriptions; `build.sh [publish]`); SEO checklist; Allen reviews the descriptions
- [ ] Publish (delete old `jb/_build/` first); `Sitemap:` in `~/AllenDowney.github.io/robots.txt`; Search Console; GreenTeaPress Task 22
- [ ] Hub entry, repo description and topics (now: "An introduction to Bayesian statistics using Python"; `bayesian-statistics`, `python`, `tutorial`)

**7. Close**
- [ ] Tag `2026-refresh`; note in GreenTeaPress Task 24

### Inventory (2026-10-19)

**The tutorial (13 notebooks; student versions at the root, solutions in `solutions/` under the same names):**

| Notebook | Topic | Data |
|---|---|---|
| `01_linda` | The laws of probability (Linda problem) | `gss_bayes.csv` |
| `02_bayes` | Bayes's theorem | `gss_bayes.csv`, `theorem1_venn_diagram.png` |
| `03_cookie` | The cookie problem | |
| `04_dice` | The dice problem | `card_venn_diagram.png`, `theorem4_venn_diagram.png` |
| `05_test` | Medical tests | |
| `06_pmf` | Probability mass functions | |
| `07_euro` | The Euro problem | |
| `08_soccer` | The World Cup problem | |
| `09_predict` | Prediction | |
| `10_joint` | Joint probability | `gss_bayes.csv` |
| `11_faceoff` | Comparisons | |
| `12_binomial` | The binomial distribution | |
| `13_price` | *The Price Is Right* problem | `showcases.2011.csv`, `showcases.2012.csv` |

Each notebook's first code cells download `utils.py` and its data from `raw/master` if missing. Imports: numpy, pandas, matplotlib, scipy (and IPython in `05_test`). Kernel metadata: Python 3.7.10. Student versions have no outputs; solutions are executed. The student versions are made from the solutions by `build.sh` (copies `solutions/[01]*.ipynb` to the root, then `remove_soln.py` replaces `# Solution` cells with `# Solution goes here`).

**Extras (kept, Allen 2026-10-19):** `bandit` (student and solution), `monty` (student and solution; needs sympy), `solutions/gps.ipynb`, `solutions/flea_beetle_soln.ipynb` (committed 2026-10-19 from an untracked 2021 file; uses `flea_beetles.csv`), `clean_gss_bayes.ipynb` (makes `gss_bayes.csv` from `gss_bayes.tar.gz` / `gss_bayes.hdf5`).

**Helpers and tools:** `utils.py` (GSS readers and `decorate`; `FixedWidthVariables` uses `np.int`), `build.sh` + `remove_soln.py` (student versions), `solutions/test.sh` (nbmake), `jb/` (Jupyter Book 1: `_config.yml` with `execute_notebooks: off`, `_toc.yml` with the README as landing page, `prep_notebooks.py` tags `# Solution` cells `remove-cell`, `build.sh` copies the solutions and publishes with ghp-import). Root `_config.yml` (Jekyll minimal theme) is unused, since Pages serves `gh-pages`.

**Removed from `master` (2026-10-19; in the tag and history):** `difference`, `elvis`, `florida` (with `GirlNamedFlorida1/2.png`, `birth_data_1935.png`), `sat_percentiles.png`, unused `run_on_colab*.png`, `scrub_code.py`, `solutions/build.sh` (pushed to "ElementsOfDataScienceSolutions", copied from another repo).

**Local state not in git (discarded 2026-10-19, backed up to the session scratchpad):** `jb/*.ipynb` and `jb/_build/` (2021 build output; now in `.gitignore`), `percentiles.ipynb` (2020, broken), `solutions/add_header.py`, `header.ipynb`, `rename.py` (2021 tooling), `solutions/regress_soln.ipynb` (PyMC3 + thinkbayes2), `solutions/two_dice_soln.ipynb` (broken), duplicate copies of the CSVs and `utils.py` in `solutions/`, `__pycache__/`.

**Runs on current libraries (2026-10-19, scratch copies, warnings as errors):** all solution notebooks run except:
- `10_joint`: `pd.crosstab(gss['partyid'], gss['polviews'])` raises "cannot reindex on an axis with duplicate labels" (pandas 3)
- `clean_gss_bayes`: `np.int` (removed in NumPy 1.24), in `utils.FixedWidthVariables`
- Not yet run: the student versions of the 13 (`bandit.ipynb` fails on its `____` blanks, as expected)

### Decisions (Allen, 2026-10-19)

- Untracked files discarded except `solutions/flea_beetle_soln.ipynb`, committed as an extra.
- Extras kept: `bandit`, `monty`, `gps`, `flea_beetle_soln`, `clean_gss_bayes`; the others deleted (above).
- Tags: only `pre-refresh-2026`.
- Layout stays: student versions at the root, solutions in `solutions/` with the same names (existing Colab links point to the root).

### Content issues

(For Allen to decide.)

1. License mismatch: the notebooks say CC BY-NC-SA 4.0; `LICENSE` is MIT.
2. README says "Python and (coming soon) R" and "a work in progress".
3. Copyright lines in the notebooks say 2020.
