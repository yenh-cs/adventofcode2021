import numpy as np

def get_data(file_name: str):
    with open(file_name) as file:
        lines= file.readlines()

        x_coordinates = [int(line.split(',')[0]) for line in lines if ',' in line]
        y_coordinates = [int(line.split(',')[1]) for line in lines if ',' in line]

        folds = [line.split(' ')[2].rstrip() for line in lines if '=' in line]
        folds = [(fold.split('=')[0], int(fold.split('=')[1])) for fold in folds]

    return x_coordinates, y_coordinates, folds


def generate_transparent_paper(x_coordinates, y_coordinates):
    paper = np.zeros((max(y_coordinates) + 1, max(x_coordinates) + 1) , dtype='int')

    for row, col in zip(y_coordinates, x_coordinates):
        paper[row][col] = 1

    return paper


def fold_vertical(paper, x):
    Y, X = paper.shape
    for i in range(Y):
        for j in range(x + 1, X):
            paper[i, 2 * x - j] = paper[i, 2 * x - j] | paper[i, j]
            paper[i, j] = 0
    return paper[:Y, :(x + 1)]


def fold_horizontal(paper, y):
    Y, X = paper.shape
    for i in range(y + 1, Y):
        for j in range(X):
            paper[2 * y - i, j] = paper[i, j] | paper[2 * y - i, j]
            paper[i, j] = 0

    return paper[:(y + 1), :X]


def fold_paper(paper, folds, n_folds=1):
    for i in range(n_folds):
        if folds[i][0] == 'x':
            paper = fold_vertical(paper, x=folds[i][1])
        else:
            paper = fold_horizontal(paper, y=folds[i][1])

    return paper


def main():
    x_coordinates, y_coordinates, folds = get_data('input.txt')
    paper = generate_transparent_paper(x_coordinates, y_coordinates)
    paper = fold_paper(paper, folds, len(folds))
    dots = (paper == 1).sum()
    print(dots)
    for line in paper:
        print("".join(["#" if point==1 else "." for point in line]))


if __name__ == '__main__':
    main()
