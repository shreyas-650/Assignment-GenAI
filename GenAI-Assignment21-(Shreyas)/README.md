# 🍷 Wine Quality Prediction using ANN

An Artificial Neural Network (ANN) regression project that predicts wine
quality from physicochemical properties. The notebook uses **KerasTuner
Random Search** to tune model hyperparameters.

## Dataset

This project uses the **Wine Quality -- White** dataset
(`winequality-white.csv`) from the UCI Machine Learning Repository.

-   **Target:** `quality`
-   **Input features:** 11 physicochemical measurements, including
    acidity, residual sugar, chlorides, density, pH, sulphates, and
    alcohol.
-   **Task:** Regression
-   **CSV separator:** Semicolon (`;`)

Load the dataset with:

``` python
df = pd.read_csv("winequality-white.csv", sep=";")
```

## Workflow

1.  Load and inspect the dataset.
2.  Check missing values and duplicate rows.
3.  Separate features (`X`) from the target (`Y = quality`).
4.  Split the data into training, validation, and test sets.
5.  Standardize features using `StandardScaler`, fitting it only on the
    training set.
6.  Build an ANN with ReLU hidden layers and a linear output layer.
7.  Tune hidden layers, neurons, dropout, and optimizer using KerasTuner
    Random Search.
8.  Evaluate the selected model on the held-out test set.

## Model Configuration

-   **Hidden-layer activation:** ReLU
-   **Output layer:** One neuron with linear activation
-   **Loss function:** Mean Squared Error (MSE)
-   **Metric:** Mean Absolute Error (MAE)
-   **Hyperparameter tuning:** KerasTuner Random Search
-   **Regularization:** Dropout

## Results

  Metric         Value
  ----------- --------
  Test Loss     0.6353
  Test MAE      0.6046

## Dataset Source

UCI Machine Learning Repository:
https://archive.ics.uci.edu/dataset/186/wine+quality
