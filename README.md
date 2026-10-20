# Bite Size Bayes

[![tests](https://github.com/AllenDowney/BiteSizeBayes/actions/workflows/tests.yml/badge.svg)](https://github.com/AllenDowney/BiteSizeBayes/actions/workflows/tests.yml)

[Allen Downey](https://allendowney.com)

*Bite Size Bayes* is an introduction to probability and Bayesian statistics using Python. It starts from scratch, with no previous knowledge of probability or Bayesian methods, and works up to Bayesian estimation, prediction and decision analysis, in short notebooks you can run on Colab.

It uses only basic Python and pandas: each problem is solved with a Bayes table or a distribution stored in a pandas `Series`, so you can see every step of the computation.

You can [read the notebooks online](https://allendowney.github.io/BiteSizeBayes/), or run them on Colab with the links below.

This is one of [my workshops and tutorials](https://allendowney.github.io/#workshops).

Suggestions are welcome: the best way to give feedback is to [create an issue in this repository](https://github.com/AllenDowney/BiteSizeBayes/issues).

**Level:** beginner. You should be comfortable with basic Python; some experience with pandas helps. You don't need any background in probability or statistics.

## Outline

1. **The Linda problem:** probability, conjunction and conditional probability, using data from the General Social Survey.
2. **Bayes's theorem:** three theorems that follow from the definitions, ending with Bayes's theorem.
3. **The cookie problem:** a first Bayesian update, and the Bayes table.
4. **The dice problem:** more than two hypotheses, and why the Bayes table works.
5. **Medical tests:** interpreting a positive test result, and the Elvis problem.
6. **Probability mass functions:** the 101 Bowls problem and the dice problem, with PMFs.
7. **The Euro problem:** estimating the probability that a coin lands heads; summarizing the posterior with credible intervals.
8. **The World Cup problem:** goal-scoring rates and the Poisson distribution.
9. **Prediction:** using posterior distributions to predict the outcome of a rematch.
10. **Joint distributions:** cross tabulation, and joint, conditional and marginal distributions.
11. **Comparisons:** a Bayesian update with two unknown quantities, the heights of two people.
12. **The binomial distribution:** the Euro problem revisited, and Bayes factors.
13. **The *Price Is Right* problem:** kernel density estimation, and using the posterior distribution to choose the best bid.

Each notebook comes in two versions: one with blanks for the exercises, and one with solutions.

| Notebook | Exercises | Solutions |
|---|---|---|
| 1. The Linda problem | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/01_linda.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/01_linda.ipynb) |
| 2. Bayes's theorem | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/02_bayes.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/02_bayes.ipynb) |
| 3. The cookie problem | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/03_cookie.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/03_cookie.ipynb) |
| 4. The dice problem | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/04_dice.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/04_dice.ipynb) |
| 5. Medical tests | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/05_test.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/05_test.ipynb) |
| 6. Probability mass functions | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/06_pmf.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/06_pmf.ipynb) |
| 7. The Euro problem | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/07_euro.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/07_euro.ipynb) |
| 8. The World Cup problem | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/08_soccer.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/08_soccer.ipynb) |
| 9. Prediction | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/09_predict.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/09_predict.ipynb) |
| 10. Joint distributions | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/10_joint.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/10_joint.ipynb) |
| 11. Comparisons | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/11_faceoff.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/11_faceoff.ipynb) |
| 12. The binomial distribution | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/12_binomial.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/12_binomial.ipynb) |
| 13. The *Price Is Right* problem | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/13_price.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/13_price.ipynb) |

## More examples

These notebooks are not part of the sequence, but they use the same methods.

| Notebook | Exercises | Solutions |
|---|---|---|
| The Bayesian bandit | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/bandit.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/bandit.ipynb) |
| The Monty Hall problem | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/monty.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/monty.ipynb) |
| The GPS problem | | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/gps.ipynb) |
| The flea beetle problem | | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/solutions/flea_beetle_soln.ipynb) |
| The Elvis problem | | [Run on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/elvis.ipynb) |

[`clean_gss_bayes.ipynb`](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/clean_gss_bayes.ipynb) shows how I made `gss_bayes.csv`, the General Social Survey data used in notebooks 1, 2 and 10.

## Running the notebooks

The easiest way to run the notebooks is on Colab: click one of the links above. You need a Google account, but you don't have to install anything. Each notebook downloads the files it needs.

To run them on your own computer, you need Python 3 with Jupyter, NumPy, pandas, SciPy, and Matplotlib (and SymPy for the Monty Hall notebook). You can [download the code in this zip file](https://github.com/AllenDowney/BiteSizeBayes/archive/master.zip), or clone the repository:

```
git clone https://github.com/AllenDowney/BiteSizeBayes
cd BiteSizeBayes
```

Then install the packages with pip:

```
pip install -r requirements.txt
```

Or, if you use conda or mamba, create an environment:

```
mamba env create -f environment.yml
mamba activate BiteSizeBayes
```

Then run `jupyter lab` and open `01_linda.ipynb`.

## Next steps

To go further, read [*Think Bayes*](https://allendowney.github.io/ThinkBayes2/), which is free online, or see [my other workshops](https://allendowney.github.io/#workshops), including ones on Bayesian decision analysis and on PyMC.

## License

The code is available under the [MIT License](LICENSE). The text is available under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).
