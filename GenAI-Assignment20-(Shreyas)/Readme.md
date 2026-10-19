# Wine Quality Prediction using ANN

An Artificial Neural Network (ANN) regression project that predicts the
quality score of red wine from its physicochemical properties. The
notebook uses **KerasTuner Random Search** to tune model
hyperparameters.

## Dataset

Use the **Wine Quality -- Red** dataset (`winequality-red.csv`) from the
UCI Machine Learning Repository.

-   **Target:** `quality`
-   **Input features:** 11 physicochemical measurements, including
    acidity, residual sugar, chlorides, density, pH, sulphates, and
    alcohol.
-   **Task:** Regression. The model predicts a numerical quality score.
-   **CSV format:** This dataset uses semicolons (`;`) as separators.

Place the dataset in the project root and name it `data.csv`, or update
the filename in the notebook.

## Workflow

1.  Load the CSV with `sep=';'`.
2.  Inspect missing values and remove duplicate rows.
3.  Separate features (`X`) from the target (`Y = quality`).
4.  Split the data into training, validation, and test sets.
5.  Standardize features with `StandardScaler`, fitting it only on the
    training set.
6.  Build an ANN with ReLU hidden layers and a linear output layer.
7.  Use KerasTuner `RandomSearch` to tune the number of hidden layers,
    neurons, dropout rate, and optimizer.
8.  Retrain the selected model with early stopping.
9.  Evaluate final performance on the held-out test set using test loss
    and MAE.

## Model configuration

-   **Hidden activation:** ReLU
-   **Output layer:** 1 neuron with linear activation
-   **Loss:** Mean Squared Error (MSE)
-   **Metric:** Mean Absolute Error (MAE)
-   **Hyperparameter tuning:** KerasTuner Random Search
-   **Regularization:** Dropout
-   **Early stopping:** Monitors validation loss and restores the best
    weights

## Setup

Use Python 3.10 or 3.11 with a compatible TensorFlow release.

``` bash
python -m venv .venv
```

Activate the environment:

**Windows**

``` powershell
.venv\Scripts\activate
```

**macOS/Linux**

``` bash
source .venv/bin/activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Launch Jupyter:

``` bash
jupyter notebook
```

Open `app.ipynb` and run the cells from top to bottom.

## Results

The recorded experiment reported:

  Metric               Value
  ----------------- --------
  Test MSE (loss)     0.6353
  Test MAE            0.6046
  Test RMSE           0.7971
  Test R²             0.2465

These are example results from one run, not guaranteed results. Results
can vary with data splitting, model initialization, library versions,
and tuning trials. An R² of about 0.25 indicates modest predictive
performance; this project is primarily for learning ANN training and
hyperparameter tuning.

## Important notes

-   The test set should be used only for final evaluation, not for
    selecting hyperparameters.
-   The current notebook uses a relatively broad search space. More
    layers or more trials do not automatically improve performance.
-   Wine quality scores are discrete and ordinal, but this notebook
    treats them as a regression target.
-   The notebook expects the CSV file at `data.csv` unless you change
    the path.

## Project files

``` text
.
├── app.ipynb
├── data.csv                 # Add the dataset locally; do not commit it unless its license permits
├── README.md
└── requirements.txt
```

## Dataset source

UCI Machine Learning Repository:
https://archive.ics.uci.edu/dataset/186/wine+quality
