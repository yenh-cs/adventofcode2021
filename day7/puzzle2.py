import math

def gauss_sum(start, end):
    diff = abs(start-end)
    return diff*(diff+1)/2

def main():
    with open("input.txt") as file:
        data = file.read()
        positions = data.strip("\n").split(",")
        positions = [int(position) for position in positions]
        positions.sort()
        positions_sums = [(target, sum(gauss_sum(position, target) for position in positions)) for target in range(positions[0], positions[-1])]
        print(min(positions_sums, key=lambda x: x[1]))


if __name__ == '__main__':
    main()
