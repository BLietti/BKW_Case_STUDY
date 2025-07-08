#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd

# create a dataframe with lags for each varibales
def create_lagged_features(df, target_col, max_lag=3):
    df_lagged = df.copy()
    for col in df.columns:
        if col != target_col:
            for lag in range(1, max_lag + 1):
                df_lagged[f"{col}_lag{lag}"] = df[col].shift(lag)
    df_lagged = df_lagged.dropna()
    return df_lagged

def flatten_prediction_list(pred_list, start_year=2016, end_year=2035):
    years = list(range(start_year, end_year + 1))
    values = []

    # Partie 1 : années de start_year à 2024
    multi_year_array = pred_list[0].iloc[0] if isinstance(pred_list[0], pd.Series) else pred_list[0][0]
    values.extend([float(v) for v in multi_year_array])

    # Partie 2 : années de 2025 à end_year
    for item in pred_list[1:]:
        if isinstance(item, pd.Series):
            val = item.iloc[0]
        elif isinstance(item, (list, np.ndarray)):
            val = item[0]
        else:
            val = item
        values.append(float(val))

    return pd.Series(values, index=years)