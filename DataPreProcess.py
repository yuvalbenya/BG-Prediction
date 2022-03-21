import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
from statsmodels.tsa.stattools import adfuller
from numpy import log

for dirname, _, filenames in os.walk('/new_data'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

path = '4.csv'

# df.to
# df = df.rename(columns={'id': 'date', 'time': 'BG_Value'}, inplace=True)
# df2 = df.set_axis(['id', 'date', 'time', 'BG_Value'], axis=1, inplace=False)
# df = pd.DataFrame(np.empty((0, 4)))
# df = pd.read_csv(path)
df = pd.read_csv(path, sep=',')
df["-15"] = ""
df["-30"] = ""
df["-45"] = ""
df["-60"] = ""
# df.fillna('', inplace=True)
prev = ""
i = 0
for index, row in df.iterrows():
    if i >= 1:
        df.at[index, "-15"] = prev
    prev = row["value"]
    i += 1
prev = ""
i = 0
for index, row in df.iterrows():
    if i >= 2:
        df.at[index, "-30"] = prev
    prev = row["-15"]
    i += 1
prev = ""
i = 0
for index, row in df.iterrows():
    if i >= 3:
        df.at[index, "-45"] = prev
    prev = row["-30"]
    i += 1
prev = ""
i = 0
for index, row in df.iterrows():
    if i >= 4:
        df.at[index, "-60"] = prev
    prev = row["-45"]
    i += 1
print(df)

df.to_csv(path, index=False)

# for

# df.columns = [seq_1.csv", index = False)
# print(df.head())
# result = adfuller(df.value.dropna())
# print('ADF Statistic: %f' % result[0])
# print('p-value: %f' % result[1])
