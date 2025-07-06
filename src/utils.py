import os
import sys
import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    



def evaluate_models(X_train, y_train, X_test, y_test, models: dict, params: dict):
    report = {}

    try:
        for model_name, model in models.items():
            param_grid = params.get(model_name, {})

            # Setup and fit GridSearchCV
            print(param_grid)
            gs = GridSearchCV(model, param_grid, cv=3)
            gs.fit(X_train, y_train)

            # Get best model after fitting
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            # Predict with best estimator
            predictions = model.predict(X_test)

            # Store R2 score
            score = r2_score(y_test, predictions)
            report[model_name] = score

        return report

    except Exception as e:
        raise CustomException(e, sys)


def load_object(path):
    try:
        with open(path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)
        

# def evaluate_models(X_train, y_train,X_test,y_test,models,params):
#     try:
#         report = {}

#         for i in range(len(list(models))):
#             model = list(models.values())[i]
#             para=params[list(models.keys())[i]]
#             print(para)
            

#             gs = GridSearchCV(model,para,cv=3)
#             gs.fit(X_train,y_train)

#             model.set_params(**gs.best_params_)
#             model.fit(X_train,y_train)

#             #model.fit(X_train, y_train)  # Train model

#             y_train_pred = model.predict(X_train)

#             y_test_pred = model.predict(X_test)

#             train_model_score = r2_score(y_train, y_train_pred)

#             test_model_score = r2_score(y_test, y_test_pred)

#             report[list(models.keys())[i]] = test_model_score

#         return report

#     except Exception as e:
#         raise CustomException(e, sys)