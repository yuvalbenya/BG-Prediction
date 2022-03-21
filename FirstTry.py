import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from pandas.plotting import register_matplotlib_converters

df = pd.read_csv("new_data/2.csv")
# print(df["value"])
# df['value'] = df['value'].astype(int)
# print(f"Rows = {len(df)}")
# print(type(df['value']))
df_values = pd.to_numeric(df["value"])
print(df_values)
df_values.plot()
plt.show()

