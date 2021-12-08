import numpy as np

def spawn(fishes, days):
    fish_count = np.zeros(9)
    for i in range(9):
        fish_count[i] = fishes.count(i)
        
    for i in range(days):
        fish_count[8], fish_count[7], fish_count[6], fish_count[5], fish_count[4], fish_count[3], fish_count[2], fish_count[1], fish_count[0] = fish_count[0], fish_count[8], fish_count[7] + fish_count[0], fish_count[6], fish_count[5], fish_count[4], fish_count[3], fish_count[2], fish_count[1]
    return fish_count 

def main():
    with open ('input.txt') as file:
        data = file.read()
        fishes = data.strip('\n').split(',')
        fishes = [int(fish) for fish in fishes]
        fish_count = spawn(fishes, 256)
        print(fish_count.sum())

if __name__ == '__main__':
    main()
