"""Copy the solution notebooks into jb/ and prepare them for the book.

For each notebook in DESCRIPTIONS, copies the solution version (../solutions/NN_name.ipynb,
or ../elvis.ipynb, which has only one version) here, without _soln in the name, and puts
the page description in the notebook metadata (see GreenTeaPress plans/seo.md).
Also copies utils.py and the data files, so the build doesn't download them.

The notebooks already have their own H1 titles, so the headings are unchanged.
"""

import shutil
from glob import glob

import nbformat

DESCRIPTIONS = {
    '01_linda': "The laws of probability in Python, starting from scratch: probability, conjunction and "
                "conditional probability, using General Social Survey data and the Linda problem.",
    '02_bayes': "Three theorems of probability, ending with Bayes's theorem, derived and checked in Python "
                "with General Social Survey data and pandas.",
    '03_cookie': "A first Bayesian update in Python: solve the cookie problem with Bayes's theorem, "
                 "then with a Bayes table of priors, likelihoods and posteriors.",
    '04_dice': "Bayes tables with more than two hypotheses: solve the dice problem in Python, "
               "and see why the Bayes table works, using the law of total probability.",
    '05_test': "Interpreting medical tests with Bayes's theorem in Python: why a positive result can be "
               "less alarming than it seems, and the Elvis problem.",
    '06_pmf': "Probability mass functions in Python with pandas: solve the 101 Bowls problem and "
              "the dice problem by representing distributions as PMFs.",
    '07_euro': "The Euro problem in Python: estimate the probability that a coin lands heads, "
               "with uniform and triangle priors, posterior means and credible intervals.",
    '08_soccer': "The World Cup problem in Python: estimate goal-scoring rates with a Bayesian update, "
                 "using the Poisson distribution and a gamma prior.",
    '09_predict': "Bayesian prediction in Python: use posterior distributions of goal-scoring rates "
                  "to predict the outcome of a World Cup rematch.",
    '10_joint': "Joint distributions in Python with pandas: cross tabulation, heatmaps, and joint, "
                "conditional and marginal distributions, using General Social Survey data.",
    '11_faceoff': "A Bayesian update with two unknowns in Python: estimate the heights of two people "
                  "from a comparison, using outer products and joint distributions.",
    '12_binomial': "The binomial distribution in Python: revisit the Euro problem, compute the evidence, "
                   "and use Bayes factors to compare hypotheses.",
    '13_price': "The Price Is Right problem in Python: kernel density estimation, a Bayesian update, "
                "and decision analysis to choose the bid with the best expected gain.",
    'bandit': "Bayesian bandits in Python: update beliefs about slot machines as you play them, "
              "then use Thompson sampling to choose which machine to play next.",
    'monty': "The Monty Hall problem in Python: solve it with a Bayes table, "
             "and check the answer symbolically with SymPy.",
    'gps': "The GPS problem in Python: infer a position in two dimensions from noisy measurements, "
           "with a joint prior, a Bayesian update and marginal posteriors.",
    'flea_beetle': "The flea beetle problem in Python: classify a beetle by species from its measurements, "
                   "using Bayes's theorem with normal likelihoods.",
    'elvis': "The Elvis problem in Python: what is the probability that Elvis was an identical twin? "
             "A Bayesian answer using 1935 birth data.",
}

SOURCES = {
    'flea_beetle': '../solutions/flea_beetle_soln.ipynb',
    'elvis': '../elvis.ipynb',
}


def prepare(name, description):
    source = SOURCES.get(name, f'../solutions/{name}.ipynb')
    nb = nbformat.read(source, 4)
    assert nb.cells[0].source.startswith('# '), name
    nb.metadata['myst'] = {'html_meta': {'description': description}}
    nb.metadata['og:description'] = description
    nbformat.write(nb, f'{name}.ipynb')
    print(f'{name} ({len(description)} characters)')


for name, description in DESCRIPTIONS.items():
    prepare(name, description)

for filename in ['../utils.py'] + glob('../*.csv') + glob('../*.png'):
    shutil.copy(filename, '.')
