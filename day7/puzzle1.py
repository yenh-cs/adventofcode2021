import math

def findMedian(nums):
    nums.sort()
    size = len(nums)
    if size%2 == 0:
        middle = int(size/2)
        median = math.floor((nums[middle] + nums[middle - 1])/2)
    else:
        middle = int(size/2 - 0.5)
        median = nums[middle] 
    return median


def findMinFuel(nums, median):
    sum = 0
    for num in nums:
        sum += abs(num - median)
    return sum


def main():
    with open("input.txt") as file:
        data = file.read()
        positions = data.strip("\n").split(",")
        positions = [int(position) for position in positions]
        median = findMedian(positions) 
        minFuel = findMinFuel(positions, median)
        print(minFuel)


if __name__ == '__main__':
    main()
