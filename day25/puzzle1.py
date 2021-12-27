import numpy as np
import pandas as pd

def get_data(file_name):
    with open(file_name) as file:
        data = file.readlines()
        data = [list(line.rstrip('\n')) for line in data]
        data = np.asarray(data)
        return data


def move_until_impossible(data, steps):
    rows, cols = data.shape
    flag = False
    # move >
    move_list = []
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == '>':
                if j == cols - 1:
                    if data[i][0] == '.':
                        move_list.append((i, j))
                else:
                    if data[i][j+1] == '.':
                        move_list.append((i, j))

    if len(move_list) != 0:
        flag = True

    for coordinate in move_list:
        row, col = coordinate[0], coordinate[1]
        if col == cols - 1:
            data[row][col] = '.'
            data[row][0] = '>'
        else:
            data[row][col] = '.'
            data[row][col + 1] = '>'

    # move v
    move_list = []
    for j in range(cols):
        for i in range(rows):
            if data[i][j] == 'v':
                if i == rows- 1:
                    if data[0][j] == '.':
                        move_list.append((i, j))
                else:
                    if data[i+1][j] == '.':
                        move_list.append((i, j))

    if len(move_list) != 0:
        flag = True

    for coordinate in move_list:
        row, col = coordinate[0], coordinate[1]
        if row == rows - 1:
            data[row][col] = '.'
            data[0][col] = 'v'
        else:
            data[row][col] = '.'
            data[row + 1][col] = 'v'

    steps += 1
    if flag:
        move_until_impossible(data, steps)

    return steps


def main():
    data = get_data('input1.txt')
    move_until_impossible(data, 0)


if __name__ == '__main__':
    main()
