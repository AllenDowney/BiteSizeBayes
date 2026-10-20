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
- [x] Env: `BiteSizeBayes` (Python 3.12.15, NumPy 2.5, pandas 3.0, SciPy 1.18, Matplotlib 3.11)

**1. Runs in a current environment**
- [x] `environment.yml` rewritten (2026-10-20): Python 3.12, conda-forge, numpy, pandas, scipy, matplotlib, sympy (monty), Jupyter, pytest, nbmake, site build tools; `empiricaldist`, `pytables` and `seaborn` dropped (none imported)
- [x] `requirements.txt` (unpinned; Colab already has all six) and `requirements-dev.txt`
- [x] First code cell: the notebooks already download `utils.py` and their data; Colab has every library, so no install cell
- [x] Breakage: `10_joint` reads `gss_bayes.csv` without `index_col=0` (pandas 3 `crosstab` fails on the duplicate `caseid` index); `utils.py` `np.int` → `int`; `clean_gss_bayes`: `replace_invalid` assigns the column (with copy-on-write the in-place `replace` silently did nothing, so the output kept invalid codes), and it extracts the tarball when `GSS.dct` is missing. It now reproduces `gss_bayes.csv` byte for byte. No deprecation warnings: all notebooks run with Deprecation/Future/PendingDeprecation/User/Runtime warnings as errors
- [x] `http://` raw URL in `13_price` → `https://`
- [x] README install section: Colab, then pip or mamba; NBViewer links dropped (Allen)

**2. Tests and CI**
- [x] `pytest --nbmake` on `solutions/*.ipynb`, the 13 student versions (their blanks are placeholders), `monty`, `elvis`, `clean_gss_bayes`: 33 pass. Left out: the student version of `bandit` (its `____` blanks don't run)
- [x] `.github/workflows/tests.yml` (push to master, PR, monthly, manual; Python 3.12; pip; 30-minute timeout; copies `utils.py` and the data into `solutions/` so CI tests this commit's versions), badge in the README. First run passed (2026-10-20, 2.5 minutes)

**3. Colab**
- [x] Colab cell after the title of each notebook (solutions also link to the version with blanks); `remove_soln.py` rewrites it for the student versions; Colab links in the README tables
- [ ] Allen runs one notebook on Colab end to end (pushed 2026-10-20)

**4. Text**
- [x] Typos (codespell): probabilies, expecially, conditonal, priod → prior, probabily (×2), conjuction, distrubution, Probablistic, oppenent, probabilites, actualy, "maximizes your the expected gain"
- [x] Links: `05_dice.ipynb` → `04_dice.ipynb`; http → https (MacKay, Gelman, GSS); redirects followed (Davidson-Pilon's book → dataorigami.net, nbviewer.org, LessWrong, matplotlib `stable/`); sci-hub → DOI links (Allen); GSS FAQ → `faq.html`; dead census.gov NAICS link dropped, text kept (Allen). The GSS Data Explorer links work (the server sends an incomplete certificate chain, so curl fails but browsers don't)
- [x] Notebook layout (2026-10-20): title cell with the "part of Bite Size Bayes" line as subtitle, then the Colab cell; copyright ("2020–2026") and license (code MIT, text CC BY-NC-SA 4.0, Allen) in a closing cell; `elvis` and `clean_gss_bayes` retitled
- [x] `13_price`: the unfinished "## Review / In this notebook" stub deleted (Allen)

**5. README in the standard shape**
- [x] Rewritten (2026-10-20): badge, author, abstract (R and "work in progress" dropped, Allen), level (beginner; no length, Allen), outline, Colab table (exercises and solutions), extras, running instructions, next steps (*Think Bayes*, hub), license (code MIT, text CC BY-NC-SA 4.0). No slides or recordings

**6. Site and visibility**
- [x] `jb/` brought up to the BayesMadeSimple template (2026-10-20): `index.md` landing page (replaces the README copy), `_toc.yml` in two parts (the 13 notebooks; "More examples": bandit, monty, gps, flea_beetle, elvis, Allen), `prep_notebooks.py` copies the solution notebooks (`flea_beetle_soln` → `flea_beetle`), `utils.py` and the data, and writes the page descriptions; `execute_notebooks: force`; pages show the solutions (Allen; the old site hid them) and link to the versions with blanks on Colab; `build.sh [publish]`
- [x] SEO checklist in a scratch build: sitemap lists the 19 pages; each has one description, one `og:description`, `rel="canonical"`; landing H1 differs from the site title; page-view counter; social image is the *Think Bayes* 2e cover
- [x] Allen approved the descriptions (2026-10-20)
- [x] Published (2026-10-20): clean `jb/_build/`, `./build.sh publish`; the old landing page `README.html` redirects to `index.html` (`jb/_extra/`, Allen); root Jekyll `_config.yml` deleted; `Sitemap:` line in `~/AllenDowney.github.io/robots.txt` (`c2af888`); live site checked
- [ ] Allen submits the sitemap in Search Console; tick in GreenTeaPress Task 22
- [x] Hub entry unchanged (still accurate); topic `jupyter-book` added (also in GreenTeaPress `scripts/repo_about.sh`); description unchanged

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

**Extras (kept, Allen 2026-10-19):** `bandit` (student and solution), `monty` (student and solution; needs sympy; both student versions now regenerated from the solutions by `build.sh`), `solutions/gps.ipynb`, `elvis.ipynb` (restored 2026-10-20, since `05_test` links to it), `solutions/flea_beetle_soln.ipynb` (committed 2026-10-19 from an untracked 2021 file; uses `flea_beetles.csv`), `clean_gss_bayes.ipynb` (makes `gss_bayes.csv` from `gss_bayes.tar.gz` / `gss_bayes.hdf5`).

**Helpers and tools:** `utils.py` (GSS readers and `decorate`; `FixedWidthVariables` uses `np.int`), `build.sh` + `remove_soln.py` (student versions), `solutions/test.sh` (nbmake), `jb/` (Jupyter Book 1: `_config.yml` with `execute_notebooks: off`, `_toc.yml` with the README as landing page, `prep_notebooks.py` tags `# Solution` cells `remove-cell`, `build.sh` copies the solutions and publishes with ghp-import). Root `_config.yml` (Jekyll minimal theme) is unused, since Pages serves `gh-pages`.

**Removed from `master` (2026-10-19; in the tag and history):** `difference`, `florida` (with `GirlNamedFlorida1/2.png`), `gss_bayes.hdf5` (2026-10-20, unused), `sat_percentiles.png`, unused `run_on_colab*.png`, `scrub_code.py`, `solutions/build.sh` (pushed to "ElementsOfDataScienceSolutions", copied from another repo).

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

Resolved 2026-10-20 (Allen): license (code MIT, text CC BY-NC-SA 4.0); README R and "work in progress" lines dropped; copyright years now 2020–2026; sci-hub links, dead GSS and NAICS links, the `13_price` review stub, the `elvis` link (notebook restored).

Open:

1. `re-use` in `10_joint` (codespell suggests "reuse"); left as is.
2. `13_price` downloads the data with `!wget` while the other notebooks use the `download` function; it works on Colab and in CI.
