import pandas as pd
import numpy as np

# Solution 1
data = pd.read_csv('input.txt', header=None)
data.columns=['measure']
diffs_df = data.measure.diff().iloc[1:]
increases_df = diffs_df.loc[diffs_df>0]
print(increases_df.count())

# Solution 2
#diffs = np.where(data.diff().iloc[1:].to_numpy()<=0, 0, 1).flatten()
#increases = np.bincount(diffs)
#print(increases)
