# Recidivism Case Study

This case study is about classification and algorithmic fairness.
It is based on two articles that were published in 2016:

* "[Machine Bias](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)", by Julia Angwin, Jeff Larson, Surya Mattu and Lauren Kirchner, and published by [ProPublica](https://www.propublica.org).

* A response by Sam Corbett-Davies, Emma Pierson, Avi Feller and Sharad Goel: "[A computer program used for bail and sentencing decisions was labeled biased against blacks. It’s actually not that clear.](https://www.washingtonpost.com/news/monkey-cage/wp/2016/10/17/can-an-algorithm-be-racist-our-analysis-is-more-cautious-than-propublicas/)", published in the Washington Post.

Both articles are about [COMPAS](https://en.wikipedia.org/wiki/COMPAS_(software)), a statistical tool used in the justice system to assign defendants a "risk score" that is intended to reflect the risk that they will commit another crime if released.

The ProPublica article evaluates COMPAS as a binary classifier and compares its error rates for black and white defendants.  It concludes that COMPAS is unfair to black defendants because they are more likely to be misclassified as high risk.

In response, the Washington Post article shows that COMPAS has the same predictive value for black and white defendants.  And they explain that the test cannot have the same predictive value and the same error rates at the same time.

The purpose of this case study is to understand these conflicting claims, to learn about classification algorithms and the metrics we use to evaluate them, and to think about fairness and the ethics of data science.

If you are working through [the *Elements of Data Science* curriculum](https://allendowney.github.io/ElementsOfDataScience), you should be ready to start this
case study when you have completed Notebook 6, which covers basic Pandas, and the [Political Alignment Case Study](https://allendowney.github.io/PoliticalAlignmentCaseStudy), which introduces cross-tabulation and some of the other tools we'll use.


## The notebooks

* [In the first notebook](https://colab.research.google.com/github/AllenDowney/RecidivismCaseStudy/blob/master/01_classification.ipynb) I replicate the analysis from the ProPublica article and define the basic metrics we use to evaluate classification algorithms, including error rates and predictive values.

* [In the second notebook](https://colab.research.google.com/github/AllenDowney/RecidivismCaseStudy/blob/master/02_calibration.ipynb) I replicate the analysis from the WaPo article and define the calibration curve, the ROC curve, and a related metric, concordance.

* [In the third notebook](https://colab.research.google.com/github/AllenDowney/RecidivismCaseStudy/blob/master/03_fairness.ipynb) I use the same methods to evaluate the performance of COMPAS for male and female defendants, and lay out the fundamental conflict between two definitions of fairness.

These three notebooks are intended to support a module in a data science class that engages students in the context and ethical challenges of machine learning.

## Slides

I used these notebooks for a module of my [Data Science class at Olin College](https://sites.google.com/site/olinds20/).

Over the course of three class sessions, I [presented these slides](https://github.com/AllenDowney/RecidivismCaseStudy/raw/master/Recidivism%20Case%20Study.pdf) and led a discussion with students.

## Additional notebooks

This repository contains three additional notebooks with additional explorations that you might be interested in.  They are not essential to understand the issues, and they are less complete than the first three notebooks.

* [The fourth notebook](https://colab.research.google.com/github/AllenDowney/RecidivismCaseStudy/blob/master/04_matrix.ipynb) proves what I asserted in the second notebook: if you are given prevalence and error rates, you can compute predictive values; and if you are given prevalence and predictive values, you can compute error rates.

* [The fifth notebook](https://colab.research.google.com/github/AllenDowney/RecidivismCaseStudy/blob/master/05_subgroups.ipynb) demonstrates that the challenge of defining fairness between groups gets harder as we consider more groups, and identifies the groups with the highest and lowest errors and predictive values.

* [The sixth notebook](https://colab.research.google.com/github/AllenDowney/RecidivismCaseStudy/blob/master/06_error.ipynb) explores what I call "the other calibration curve", the probability of being classified high risk as a function of the probability of recidivism.

I include these notebook in part to resist the temptation to hide my development process.  I worked on this case study on and off over several years.  I explored a lot of things and took a lot of wrong turns.  It took me a long time to find the story, get it organized, and strike a balance between two conflicting goals: maintaining the scientific detachment that lets us tackle difficult topics while also keeping sight of the context, the people, and the human consequences.

I hope these materials will be engaging and informative for readers, and useful for teaching and learning the ethical practice of data science.
