import numpy as np
import pandas as pd

def split_data(row):
    row = row.iloc[0]
    row = row.split('=')[1]
    start, end = row.split('..')
    return (int(start), int(end))

def read_data(file_name):
    df = pd.read_csv(file_name, header=None, sep=' ')
    df[['x','y','z']] = df[1].str.split(',', expand=True)
    df.drop([1], axis=1, inplace=True)
    df['x'] = df[['x']].apply(split_data, axis=1)
    df['y'] = df[['y']].apply(split_data, axis=1)
    df['z'] = df[['z']].apply(split_data, axis=1)
    return df

def execute_commands(cubes, commands):
    for i in range(len(commands)):
        execute_command(cubes, commands.iloc[i, :])

def execute_command(cubes, command):
    if (command['x'][0] < -50 or command['x'][1] > 50) or\
        (command['y'][0] < -50 or command['y'][1] > 50) or\
        (command['z'][0] < -50 or command['z'][1] > 50):
        return

    if command[0] == 'on':
        for i in range(command['x'][0] + 50, command['x'][1] + 51):
            for j in range(command['y'][0] + 50, command['y'][1] + 51):
                for k in range(command['z'][0] + 50, command['z'][1] + 51):
                    cubes[i][j][k] = 1
    else:
        for i in range(command['x'][0] + 50, command['x'][1] + 51):
            for j in range(command['y'][0] + 50, command['y'][1] + 51):
                for k in range(command['z'][0] + 50, command['z'][1] + 51):
                    cubes[i][j][k] = 0


def count(cubes):
    count = 0
    for i in range(101):
        for j in range(101):
            for k in range(101):
                if cubes[i][j][k] == 1:
                    count += 1
    return count


def main():
    commands = read_data('input2.txt')
    print(commands)
    cubes = []
    for i in range(101):
        cubes.append([])
        for j in range(101):
            cubes[i].append([])
            for k in range(101):
                cubes[i][j].append(0)

    execute_commands(cubes, commands)
    print(count(cubes))

if __name__ == '__main__':
    main()
