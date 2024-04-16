import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import imputer, scaler

def preprocess_dataset(dataset):
    for column in dataset.columns:

        if dataset[column].dtype == object:
            most_common_value = dataset[column].mode()[0]
            dataset[column].fillna(most_common_value, inplace=True)
        
        elif dataset[column].dtype == np.number:
            dataset[column] = imputer(dataset[column])

    return dataset

# IDEAS #
# Identificar columnas numéricas y categóricas
# numeric_cols = df.select_dtypes(include=[np.number]).columns
# categorical_cols = df.select_dtypes(include=['object']).columns

