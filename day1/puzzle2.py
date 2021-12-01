import pandas as pd
import numpy as np
from collections import deque

def window(seq, size=2):
    it = iter(seq)
    win = deque((next(it, None) for _ in range(size)), maxlen=size)
    yield win
    append = win.append
    for e in it:
        append(e)
        yield win

data = pd.read_csv('input.txt', header=None)
data = data.to_numpy().flatten()

windowed_data = []
for each in window(data, 3):
    window_sum = sum(each)
    windowed_data.append([window_sum])

windowed_data = pd.Series(np.array(windowed_data).flatten())
window_diffs = windowed_data.diff().iloc[1:]
increases_df = window_diffs.loc[window_diffs>0]
print(increases_df.count())
