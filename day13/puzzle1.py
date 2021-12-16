import pandas as pd
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
    right_part = x*2 + 1 if X >= x*2 + 1 else X
    for i in range(Y):
        count = 2
        for j in range(x + 1, right_part):
            if paper[i][j] == 1:
                paper[i][j] = 0
                paper[i][j-count] = 1
            count += 2 


def fold_horizontal(paper, y):
    Y, X = paper.shape
    bottom_part = y*2 + 1 if Y >= y*2 + 1 else Y
    count = 2
    for i in range(y + 1, bottom_part):
        for j in range(X):
            if paper[i][j] == 1:
                paper[i][j] = 0
                paper[i-count][j] = 1
        count += 2 


def fold_paper(paper, folds, n_folds=1):
    for i in range(n_folds):
        if folds[i][0] == 'x':
            fold_vertical(paper, x=folds[i][1])
        else:
            fold_horizontal(paper, y=folds[i][1])



def main():
    x_coordinates, y_coordinates, folds = get_data('input.txt')
    paper = generate_transparent_paper(x_coordinates, y_coordinates)
    fold_paper(paper, folds, 2)
    dots = (paper == 1).sum()
    print(dots)


if __name__ == '__main__':
    main()
