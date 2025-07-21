# Spaceship Titanic: Predictive Modeling Project

This repository contains the code and documentation for a predictive modeling solution to the Kaggle "Spaceship Titanic" competition. The primary goal is to predict whether a passenger was transported to an alternate dimension during a deep-space anomaly.

## Project Overview

The project involves a binary classification task using passenger data from a fictional starship. This notebook walks through the complete data science pipeline:

* Initial data exploration
* Extensive feature engineering
* Model training and evaluation
* Final predictions using a high-performance stacking ensemble

## Feature Engineering

To enhance the model's predictive power, new features were engineered. This step was critical to uncovering hidden patterns and relationships in the dataset.

| Feature Name         | Source Column(s)    | Description                                                                                               | Rationale                                                                                                    |
| -------------------- | ------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Deck, Side, CabinNum | Cabin               | The Cabin column (e.g., "F/123/S") was split into three features: Deck (F), CabinNum (123), and Side (S). | Cabin location provides spatial context, which is a strong predictor. Decomposing it allows better learning. |
| GroupSize            | PassengerId         | Passenger IDs like "0014\_02" indicate travel groups. This feature counts the number of people per group. | Group dynamics influence outcomes; people in groups may behave differently than solo travelers.              |
| IsAlone              | GroupSize           | A binary feature: True if GroupSize == 1, otherwise False.                                                | A simplified signal capturing the group effect.                                                              |
| TotalSpend           | Expenditure Columns | Sum of: RoomService, FoodCourt, ShoppingMall, Spa, VRDeck.                                                | Reflects total economic activity—often tied to status and outcomes.                                          |
| HasSpent             | TotalSpend          | A binary flag: True if TotalSpend > 0.                                                                    | Indicates whether a passenger was active economically, potentially linked to CryoSleep status.               |
| AgeGroup             | Age                 | Age was binned into: "Child", "Teen", "Adult", "Senior".                                                  | Captures non-linear effects of age. Categorization reveals insights lost in raw numeric form.                |

## Modeling Approach: Stacking Ensemble

Rather than using a single model, a stacking ensemble approach was implemented to maximize predictive accuracy. This strategy blends multiple base models and trains a final meta-model to optimize the final predictions.

### Model Architecture

* Base Models

  * XGBoost (Extreme Gradient Boosting): Efficient and powerful model tailored for structured/tabular data.
  * LightGBM (Light Gradient Boosting Machine): Fast and memory-efficient model that handles large datasets effectively.

* Meta-Model

  * Logistic Regression: A simple linear model that combines the predictions of the base models to generate the final binary output.

## Advantages of the Stacking Ensemble

| Benefit               | Description                                                                                                      |
| --------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Improved Accuracy     | Leverages the strengths of multiple models to detect complex data patterns.                                      |
| Better Generalization | Reduces the risk of overfitting by balancing individual model biases.                                            |
| Model Diversity       | XGBoost and LightGBM have different learning mechanisms, helping the ensemble correct a broader range of errors. |
| Competitive Edge      | Stacking is a proven strategy in top Kaggle competitions, often resulting in state-of-the-art solutions.         |

For detailed code and results, refer to the notebooks and scripts provided in this repository.
# Spaceship Titanic: Predictive Modeling Project

This repository contains the code and documentation for a predictive modeling solution to the Kaggle "Spaceship Titanic" competition. The primary goal is to predict whether a passenger was transported to an alternate dimension during a deep-space anomaly.

## Project Overview

The project involves a binary classification task using passenger data from a fictional starship. This notebook walks through the complete data science pipeline:

* Initial data exploration
* Extensive feature engineering
* Model training and evaluation
* Final predictions using a high-performance stacking ensemble

## Feature Engineering

To enhance the model's predictive power, new features were engineered. This step was critical to uncovering hidden patterns and relationships in the dataset.

| Feature Name         | Source Column(s)    | Description                                                                                               | Rationale                                                                                                    |
| -------------------- | ------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Deck, Side, CabinNum | Cabin               | The Cabin column (e.g., "F/123/S") was split into three features: Deck (F), CabinNum (123), and Side (S). | Cabin location provides spatial context, which is a strong predictor. Decomposing it allows better learning. |
| GroupSize            | PassengerId         | Passenger IDs like "0014\_02" indicate travel groups. This feature counts the number of people per group. | Group dynamics influence outcomes; people in groups may behave differently than solo travelers.              |
| IsAlone              | GroupSize           | A binary feature: True if GroupSize == 1, otherwise False.                                                | A simplified signal capturing the group effect.                                                              |
| TotalSpend           | Expenditure Columns | Sum of: RoomService, FoodCourt, ShoppingMall, Spa, VRDeck.                                                | Reflects total economic activity—often tied to status and outcomes.                                          |
| HasSpent             | TotalSpend          | A binary flag: True if TotalSpend > 0.                                                                    | Indicates whether a passenger was active economically, potentially linked to CryoSleep status.               |
| AgeGroup             | Age                 | Age was binned into: "Child", "Teen", "Adult", "Senior".                                                  | Captures non-linear effects of age. Categorization reveals insights lost in raw numeric form.                |

## Modeling Approach: Stacking Ensemble

Rather than using a single model, a stacking ensemble approach was implemented to maximize predictive accuracy. This strategy blends multiple base models and trains a final meta-model to optimize the final predictions.

### Model Architecture

* Base Models

  * XGBoost (Extreme Gradient Boosting): Efficient and powerful model tailored for structured/tabular data.
  * LightGBM (Light Gradient Boosting Machine): Fast and memory-efficient model that handles large datasets effectively.

* Meta-Model

  * Logistic Regression: A simple linear model that combines the predictions of the base models to generate the final binary output.

## Advantages of the Stacking Ensemble

| Benefit               | Description                                                                                                      |
| --------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Improved Accuracy     | Leverages the strengths of multiple models to detect complex data patterns.                                      |
| Better Generalization | Reduces the risk of overfitting by balancing individual model biases.                                            |
| Model Diversity       | XGBoost and LightGBM have different learning mechanisms, helping the ensemble correct a broader range of errors. |
| Competitive Edge      | Stacking is a proven strategy in top Kaggle competitions, often resulting in state-of-the-art solutions.         |

For detailed code and results, refer to the notebooks and scripts provided in this repository.
