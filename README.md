# Titanic Passenger Survival Prediction

![Titanic](https://cdn.britannica.com/79/4679-050-BC127236/Titanic.jpg)

## Overview

This project builds a machine learning model to predict whether a passenger aboard the RMS Titanic would survive or not based on various attributes such as passenger class, age, fare, and other demographic features.

Visit kaggle notebook :- https://www.kaggle.com/code/pranjalsapkota/titanic-survival-predictor?scriptVersionId=302683179

#### The model's cross validation accuracy was around 83.47% for Random Forest and 83.02% for XGBoost

## Updates:
* 17th Mar 2026: Implemented fastAPI. Test the api on 
https://titanic-survival-predictor-7ebg.onrender.com/
(Its a free tier render deployment so the service might be sleeping)

## Dataset

The dataset used in this project contains passenger information from the Titanic disaster in 1912.
https://www.kaggle.com/datasets/smirkxd/titanic-dataset

Typical features in the dataset include:

* PassengerId
* Pclass (Ticket class)
* Name
* Sex
* Age
* SibSp (Number of siblings/spouses aboard)
* Parch (Number of parents/children aboard)
* Ticket
* Fare
* Cabin
* Embarked
* Survived (Target variable)

Target variable:

* **Survived**

  * 0 → Did not survive
  * 1 → Survived

## Project Workflow

1. Environmental Setup
2. Loading Dataset
3. Initial Data Cleaning
4. Encode categorical variables
5. Define features and target
6. Split dataset
7. Train models
8. Evaluate models
9. Analyzing feature importance
10. Improving model
11. Cross validation and confusion matrix
12. Create input sample

## Model Used

* Random Forest Classifier
* XGBoost Classifier

## Example Prediction Input

Example passenger data:

* Pclass: 3
* Sex: Male
* Age: 22
* Fare: 12.36

The model predicts whether the passenger **survived or not**.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Jupyter Notebook

## References

* Kaggle Titanic Dataset
* Scikit-learn Documentation

