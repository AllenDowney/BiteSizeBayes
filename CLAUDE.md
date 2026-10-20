# BiteSizeBayes

Allen Downey's tutorial *Bite Size Bayes*: a self-paced introduction to probability and Bayesian statistics in Python (pandas, NumPy, SciPy), with no previous knowledge assumed. Not given as a live workshop. The site is a Jupyter Book 1 build (`jb/`) published to `gh-pages`: `allendowney.github.io/BiteSizeBayes/`.

**Guide for the 2026 refresh:** the "Refresh checklist" in `~/GreenTeaPress/plans/workshops.md`. Progress goes on `PROJECT_BOARD.md` here (Task 1) and in GreenTeaPress Task 24.

## Which notebooks are the tutorial

Thirteen notebooks, `01_linda` to `13_price`. The solution versions are in `solutions/` with the same names; the student versions at the root are generated from them by `build.sh` (`remove_soln.py` replaces cells that start with `# Solution` by `# Solution goes here`). Edit the solutions and regenerate; don't edit the root versions by hand.

Extras, not part of the sequence: `bandit` and `monty` (both versions), `solutions/gps.ipynb`, `solutions/flea_beetle_soln.ipynb`, `elvis.ipynb`, and `clean_gss_bayes.ipynb` (makes `gss_bayes.csv`).

Each notebook downloads `utils.py` and its data files from `raw/master` if they are missing, so keep those files at the repo root and keep the branch name `master`.

## Tags

- `pre-refresh-2026`: the state before the 2026 refresh. There are no recordings to tag.

## Testing

Environment: mamba env `BiteSizeBayes` (Python 3.12). Run the solution notebooks top to bottom:

```
pytest --nbmake solutions/*.ipynb [01]*.ipynb monty.ipynb elvis.ipynb clean_gss_bayes.ipynb
```

The target environment is Google Colab's current Python and libraries.

## Conventions

- Don't change the substance of the text; list content questions under "Content issues" on the board for Allen to decide.
- Keep student and solution versions in sync (regenerate the root versions with the copy and `remove_soln.py` steps of `build.sh`; the script also commits and pushes).
