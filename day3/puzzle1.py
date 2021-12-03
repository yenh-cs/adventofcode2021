import pandas as pd
import numpy as np

data = pd.read_csv('input.txt', header=None, dtype='str')
data = data[0].str.split('', expand=True)
data[0] = np.nan
data[13] = np.nan
data = data.dropna(axis=1, how='any')

gamma_rate = []
epsilon_rate = []
for column in data:
    most_common = data[column].value_counts().idxmax()
    least_common = 0 if most_common == '1' else 1
    gamma_rate.append(most_common)
    epsilon_rate.append(least_common)

gamma_rate_str = ''.join(str(x) for x in gamma_rate)
epsilon_rate_str = ''.join(str(x) for x in epsilon_rate)

gamma_rate = int(gamma_rate_str, 2)
epsilon_rate = int(epsilon_rate_str, 2)
power_consumption = gamma_rate * epsilon_rate
print(gamma_rate)
print(epsilon_rate)
print(power_consumption)
