# Feature Engineering & Machine Learning Pipelines

A Python project covering feature engineering, categorical encoding, feature scaling, and end-to-end machine learning pipelines using Pandas and Scikit-learn.

## 📌 Overview

This project demonstrates essential data preprocessing techniques and how to combine them into a complete machine learning workflow using an Online Food Delivery dataset.

## 🛠️ Tech Stack

- **Language:** Python
- **Data Handling:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Techniques:** Feature Engineering, Encoding, Scaling, Pipelines, Classification

## 📂 Tasks Implemented

### Part 1: Feature Engineering

**Task 1 — Creating New Features**
- Identify existing dataset columns.
- Create meaningful features derived from existing data.
- Add new features to the DataFrame.

**Task 2 — Date & Text Features**
- Extract date components such as year, month, and day when date columns are available.
- Extract text length or word count when text columns are available.
- Explain when these operations are not applicable to the dataset.

### Part 2: Feature Encoding

**Task 3 — One-Hot Encoding**
- Identify categorical columns.
- Apply `pd.get_dummies()` to convert categorical values into numerical features.

**Task 4 — Column Transformer**
- Separate numerical and categorical features.
- Apply `OneHotEncoder` to categorical columns.
- Pass numerical columns through unchanged using `ColumnTransformer`.

### Part 3: Feature Scaling

**Task 5 — Standardization**
- Apply `StandardScaler` to numerical features.
- Transform numerical data to approximately zero mean and unit standard deviation.

**Task 6 — Normalization**
- Apply `MinMaxScaler` to scale numerical features between 0 and 1.
- Compare normalized values with standardized values.

### Part 4: Building Machine Learning Pipelines

**Task 7 — Preprocessing Pipeline**
- Create separate numerical and categorical preprocessing pipelines.
- Combine the pipelines using `ColumnTransformer`.

**Task 8 — Full Scikit-learn Pipeline**
- Handle missing numerical values using `SimpleImputer`.
- Handle missing categorical values using the most frequent value.
- Scale numerical and ordinal features.
- Encode nominal categorical features using `OneHotEncoder`.
- Combine preprocessing and Logistic Regression using `Pipeline`.
- Split the dataset into training and testing sets.
- Train the model, generate predictions, and evaluate accuracy.

## 🔄 Pipeline Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Feature Separation
     ↓
┌──────────────────┬──────────────────┐
│ Numerical        │ Categorical      │
│ Imputation       │ Imputation       │
│ Scaling          │ Encoding         │
└──────────────────┴──────────────────┘
          ↓
  ColumnTransformer
          ↓
  Logistic Regression
          ↓
   Model Predictions
          ↓
   Accuracy Evaluation
```

## 📊 Evaluation

The Logistic Regression model is evaluated using `accuracy_score` on the test dataset.

The accuracy value depends on the train-test split and dataset. Run the code to obtain the actual result.

## 📦 Installation

Install the required libraries:

```bash
pip install pandas numpy scikit-learn
```

## ▶️ Run the Project

1. Clone or download this repository.
2. Place the Online Food Delivery dataset at the path expected by your Python script.
3. Run the script or notebook containing the implementation.
4. Review the transformed features, predictions, and evaluation results.

## 🎯 Key Takeaways

- Preparing raw data for machine learning.
- Encoding categorical variables.
- Understanding standardization versus normalization.
- Combining preprocessing steps with `ColumnTransformer`.
- Building reusable end-to-end workflows with Scikit-learn's `Pipeline`.

---

**Domain:** Machine Learning | Data Preprocessing | Feature Engineering

