import numpy as np 

def getRandomNumbers(fileName):
    with open(fileName, 'r', encoding='utf-8') as rad:
        number_line = rad.read()

    random_nums = number_line.rstrip('\n').split(',')
    return [int(s) for s in random_nums]

def getBoards(fileName):
    numbers = []
    with open(fileName, 'r', encoding='utf-8') as boards:
        for line in boards:
            line = line.strip('\n')
            if line != '':
                numbers.extend([int(num) for num  in line.split(' ') if num != ''])
    boards = []
    i = 0
    limit = len(numbers)
    while i < limit:
        board = np.zeros(shape=(5,5), dtype='int32') 
        for j in range(5):
            for k in range(5):
                board[j][k] = numbers[i]
                i += 1
        boards.append(board)    
    
    return boards
    

def markNumber(num, boards, markeds):
    no_boards = len(boards)
    for i in range(no_boards):
        for j in range(5):
            for k in range(5):
                if boards[i][j][k] == int(num):
                    markeds[i][j][k] = 1;
    
    return markeds


def anyWin(num, boards, markeds):
    no_boards = len(boards)
    win = True 
    win_board = -1 
    sum_of_unmarked = 0

    for i in range(no_boards):
        # loop over rows
        for j in range(5):
            win = True
            for k in range(5):
                if markeds[i][j][k] == 0:
                    win = False
                    break
            if win == True:
                win_board = i
                break
        if win == True:
            win_board = i
            break
        
        #loop over columns
        for j in range(5):
            win = True
            for k in range(5):
                if markeds[i][k][j] == 0 :
                    win = False
                    break
            if win == True:
                win_board = i
                break
        if win == True:
            win_board = i
            break
        
    if win_board == -1:
        win = False
    else:
        for i in range(5):
            for j in range(5):
                if markeds[win_board][i][j] == 0:
                    sum_of_unmarked += boards[win_board][i][j]
    return (win, sum_of_unmarked, num)


# preprocess data
random_nums = getRandomNumbers('random.txt')
boards = getBoards('input.txt')

# initialize numbers for calculation
no_boards = len(boards)
markeds = []

for i in range(no_boards):
    markeds.append(np.zeros(shape=(5,5), dtype='int32'))
    
win=False 
i = 0
while (i<len(random_nums)) & (win==False):
    markeds = markNumber(random_nums[i], boards, markeds)
    win, sum_of_unmarked, last_called = anyWin(random_nums[i], boards, markeds)
    i += 1

print(sum_of_unmarked*last_called)
