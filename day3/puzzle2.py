import pandas as pd
import numpy as np

def calOxyGeneratorRating(df):
    for i in range(1, 13):
        counts = np.bincount(df[i])
        most_common_oxy = 0 if counts[0] > counts[1] else 1
        df = df[df[i]==str(most_common_oxy)]
        if df.shape==(1, 12):
            break
    
    oxy_rating = df.to_numpy().flatten()
    oxy_rating_bin = ''.join(oxy_rating)
    oxy_rating_dec = int(oxy_rating_bin, 2)
    return oxy_rating_dec


def calCO2ScrubberRating(df):
    for i in range(1, 13):
        counts = np.bincount(df[i])
        least_common = 0 if counts[0] <= counts[1] else 1
        df = df[df[i]==str(least_common)]
        if df.shape==(1, 12):
            break
    
    co2_rating = df.to_numpy().flatten()
    co2_rating_bin = ''.join(co2_rating)
    co2_rating_dec = int(co2_rating_bin, 2)
    return co2_rating_dec 


data = pd.read_csv('input.txt', header=None, dtype='str')
data = data[0].str.split('', expand=True)
data[0] = np.nan
data[13] = np.nan
data = data.dropna(axis=1, how='any')
oxy_rating = calOxyGeneratorRating(data)
print(oxy_rating)
co2_rating = calCO2ScrubberRating(data)
print(co2_rating)
life_support_rating = oxy_rating * co2_rating
print(life_support_rating)
