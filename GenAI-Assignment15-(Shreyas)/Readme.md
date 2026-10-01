# Assignment 15 — Core Algorithms, Metrics & Model Behavior

A hands-on Machine Learning assignment focused on implementing fundamental regression and classification algorithms, evaluating model performance using standard metrics, and understanding model behavior such as overfitting, underfitting, bias, and variance.

## Overview

This assignment covers the core concepts required to build, evaluate, and compare basic Machine Learning models using Python and scikit-learn.

The work includes:

- Regression using Linear Regression
- Regression evaluation metrics
- Classification using Logistic Regression
- Gaussian Naive Bayes classification
- K-Nearest Neighbors (KNN)
- Classification evaluation metrics
- Overfitting and underfitting
- Bias and variance concepts

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Dataset

The assignment uses Kaggle datasets as specified in the assignment requirements.

Two datasets were used where required:

- Car dataset — Regression
- Heart Disease dataset — Classification

### Regression Target

`selling_price`

### Classification Target

`Heart Disease Status`

## Tasks

### Part 1 — Regression Algorithm

#### Task 1: Linear Regression

Built a Linear Regression model to predict car selling prices.

Steps performed:

- Selected `selling_price` as the numerical target
- Split the dataset into training and testing sets
- Preprocessed numerical and categorical features
- Trained a Linear Regression model
- Generated predictions on the test dataset
- Plotted actual vs predicted values

### Part 2 — Regression Metrics

#### Task 2: Regression Evaluation Metrics

Evaluated the Linear Regression model using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

These metrics were used to understand the prediction error and overall regression performance.

## Part 3 — Classification Algorithms

### Task 3: Logistic Regression

Implemented Logistic Regression for binary classification.

The workflow included:

- Selecting the classification target
- Train-test split
- Feature encoding
- Feature scaling
- Model training
- Test-set predictions

### Task 4: Gaussian Naive Bayes

Implemented a Gaussian Naive Bayes classifier and compared its performance with Logistic Regression.

### Task 5: K-Nearest Neighbors

Implemented KNN classification using different values of `k`.

The effect of different values of `k` was observed and the best-performing value was selected based on accuracy.

## Part 4 — Classification Metrics

### Task 6: Classification Evaluation

The classification models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

These metrics provide different perspectives on classification performance rather than relying only on accuracy.

## Part 5 — Model Behavior & Learning Concepts

### Task 7: Overfitting & Underfitting

SVM models with different configurations were used to observe model behavior.

The comparison included:

- Training accuracy
- Testing accuracy

A simpler configuration was used to observe underfitting behavior, while a more complex configuration was used to observe potential overfitting behavior.

### Task 8: Bias & Variance

The assignment also covers the conceptual relationship between:

- Bias
- Variance
- Underfitting
- Overfitting

The task explains how model complexity affects training and testing performance and discusses approaches for reducing overfitting.

## Machine Learning Workflow

The general workflow followed throughout the assignment was:

```text
Data Loading
     ↓
Data Cleaning
     ↓
Feature & Target Separation
     ↓
Encoding
     ↓
Train-Test Split
     ↓
Feature Scaling
     ↓
Model Training
     ↓
Prediction
     ↓
Model Evaluation