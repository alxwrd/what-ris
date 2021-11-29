# Qumodo Dev Test

This test requires you to build, document and deploy an API that
provides basic math processing and exposes a Machine Learning
model we've provided for external use (prediction only).

You'll be asked to present your work during the interview.  We
will be particularly interested in how you approached the
problem; your development style and technology choices, along
with your thoughts on further development.

The choice of programming language is entirely up to you.  The
Machine Learning model is a Gaussian Naive Bayes model from
Python 3.6 SKLearn, persisted using Python 3.6 pickle.

We understand your spare-time is limited, so if you don't have
time to complete the test we are content with foundation code and
a description of how you would approach building the remainder.
(Basic production-grade code is better than a brittle solution
that covers all the requirements).

Things to consider: scalability, unit and integration testing,
security and future extensibility.

## Part 1 - Math Processing

Build an API which provides basic math processing, specifically
summing two numbers and dividing two numbers.

## Part 2 - ML Model Serving

Build an API which exposes the Machine Learning model we've
included, to enable third-parties to submit features and receive
a prediction of class as a result.

We've given you a pre-trained model `(models/iris_model.pkl)`
that implements the well-known Iris dataset.  We've also provided
a set of validation features
`(data/iris_validation_features.pkl)` and associated classes
`(data/iris_validation_classes.pkl)` in numpy format (Python 3.6
pickles), which can be used to test model operation.

The model is capable of predicting on multiple sets of features
and returning classes for each set of features; the API should
support this aswell.

Class labels are as follows:
```
[ 0: "setosa", 1: "versicolor", 2: "virginica"]
```

The expected accuracy score (Jaccard Similarity Score) for the
model using the provided validation fearures is 0.98.

More info on accurracy score: (http://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_similarity_score.html)

More info on the Iris data: (http://scikit-learn.org/stable/datasets/index.html#iris-dataset)

## Part 3 - DevOps

Generate a basic DevOps solution for deploying your API - e.g.
Docker, CircleCI

## Part 3 - Documentation

Generate documentation for the API - e.g. installation, running
locally, remote deployment, endpoint descriptions.
