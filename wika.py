import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

X = pd.read_csv("X.csv")
y = pd.read_csv("y.csv")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 335718)


param_grid = {
    'criterion': ["gini", "entropy"],
    'max_depth': [None, 10, 20, 30],
    'min_samples_leaf': [1, 5, 10],
    'min_samples_split': [2, 5, 10],
    'max_features': ["auto", "sqrt", "log2", None],
    'splitter': ["best", "random"]
    # Add other hyperparameters here
}

# Step 3: Create a Decision Tree Classifier and GridSearchCV object
clf = DecisionTreeClassifier()
grid_search = GridSearchCV(clf, param_grid, cv=5, scoring='accuracy')

# Step 4: Fit the model with GridSearchCV
grid_search.fit(X_train, y_train)

# Step 5: Get the best parameters and best accuracy
best_params = grid_search.best_params_
best_accuracy = grid_search.best_score_
print("Best parameters:", best_params)
print("Best cross-validated accuracy:", best_accuracy)

# Step 6: Train and evaluate the decision tree on the test set with the best parameters
best_clf = DecisionTreeClassifier(**best_params)
best_clf.fit(X_train, y_train)
test_accuracy = best_clf.score(X_test, y_test)
print("Test accuracy with best parameters:", test_accuracy)