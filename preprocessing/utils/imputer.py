import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

def impute_values(vector):
    sc = SimpleImputer(strategy='median')
    return sc.fit_transform(vector)