import numpy as np

with open("input.txt") as f:
    lines = f.readlines()
    xs = [int(l.split(",")[0]) for l in lines if "," in l]
    ys = [int(l.split(",")[1]) for l in lines if "," in l]
    folds = [(l.split("=")[0][-1], int(l.split("=")[1])) for l in lines if "=" in l]

map = np.zeros((max(ys) + 1, max(xs) + 1), dtype=bool)
for x, y in zip(xs, ys):
    map[y, x] = True

for fold in folds:
    if fold[0] == "x":
        map = map[:, : map.shape[1] // 2] + map[:, map.shape[1] // 2 + 1 :][:, ::-1]
    
    if fold[0] == "y":
        map = map[: map.shape[0] // 2, :] + map[map.shape[0] // 2 + 1 :, :][::-1, :]

for line in map:
    print("".join(["#" if c else " " for c in line]))
