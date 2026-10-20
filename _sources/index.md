---
myst:
  html_meta:
    description: "A beginner's introduction to probability and Bayesian statistics in Python: 13 short notebooks that use pandas to solve problems with Bayes's theorem."
og:description: "A beginner's introduction to probability and Bayesian statistics in Python: 13 short notebooks that use pandas to solve problems with Bayes's theorem."
---

# Bite Size Bayes: An Introduction to Probability and Bayesian Statistics in Python

[Allen Downey](https://allendowney.com)

*Bite Size Bayes* is an introduction to probability and Bayesian statistics using Python. It starts from scratch, with no previous knowledge of probability or Bayesian methods, and works up to Bayesian estimation, prediction and decision analysis, in short notebooks you can run on Colab.

It uses only basic Python and pandas: each problem is solved with a Bayes table or a distribution stored in a pandas `Series`, so you can see every step of the computation.

**Level:** beginner. You should be comfortable with basic Python; some experience with pandas helps. You don't need any background in probability or statistics.

## The notebooks

The pages on this site show the notebooks with solutions. To do the exercises, run the versions with blanks on Colab:

1. [The Linda problem](01_linda): probability, conjunction and conditional probability, using data from the General Social Survey. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/01_linda.ipynb)
2. [Bayes's theorem](02_bayes): three theorems that follow from the definitions, ending with Bayes's theorem. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/02_bayes.ipynb)
3. [The cookie problem](03_cookie): a first Bayesian update, and the Bayes table. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/03_cookie.ipynb)
4. [The dice problem](04_dice): more than two hypotheses, and why the Bayes table works. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/04_dice.ipynb)
5. [Medical tests](05_test): interpreting a positive test result, and the Elvis problem. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/05_test.ipynb)
6. [Probability mass functions](06_pmf): the 101 Bowls problem and the dice problem, with PMFs. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/06_pmf.ipynb)
7. [The Euro problem](07_euro): estimating the probability that a coin lands heads; summarizing the posterior with credible intervals. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/07_euro.ipynb)
8. [The World Cup problem](08_soccer): goal-scoring rates and the Poisson distribution. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/08_soccer.ipynb)
9. [Prediction](09_predict): using posterior distributions to predict the outcome of a rematch. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/09_predict.ipynb)
10. [Joint distributions](10_joint): cross tabulation, and joint, conditional and marginal distributions. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/10_joint.ipynb)
11. [Comparisons](11_faceoff): a Bayesian update with two unknown quantities, the heights of two people. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/11_faceoff.ipynb)
12. [The binomial distribution](12_binomial): the Euro problem revisited, and Bayes factors. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/12_binomial.ipynb)
13. [The *Price Is Right* problem](13_price): kernel density estimation, and using the posterior distribution to choose the best bid. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/13_price.ipynb)

## More examples

These notebooks are not part of the sequence, but they use the same methods.

- [The Bayesian bandit](bandit): Thompson sampling. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/bandit.ipynb)
- [The Monty Hall problem](monty). [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/monty.ipynb)
- [The GPS problem](gps): inferring a position in two dimensions.
- [The flea beetle problem](flea_beetle): classifying beetles by their measurements.
- [The Elvis problem](elvis): was Elvis an identical twin?

## Next steps

To go further, read [*Think Bayes*](https://allendowney.github.io/ThinkBayes2/), which is free online, or see [my other workshops](https://allendowney.github.io/#workshops).

The code is on [GitHub](https://github.com/AllenDowney/BiteSizeBayes), under the MIT License; the text is under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license.
