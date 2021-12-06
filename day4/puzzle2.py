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
    for i in range(len(boards)):
        for j in range(5):
            for k in range(5):
                if boards[i][j][k] == int(num):
                    markeds[i][j][k] = 1;
    
    return markeds


def anyWin(num, boards, markeds):
    win = True 
    win_board = -1 
    sum_of_unmarked = 0
    removed_indice = []


    for i in range(len(boards)):
        # loop over rows
        for j in range(5):
            win = True
            for k in range(5):
                if markeds[i][j][k] == 0:
                    win = False
                    break
            if win == True:
                break
        if win == True:
            for m in range(5):
                for n in range(5):
                    if markeds[win_board][m][n] == 0:
                        sum_of_unmarked += boards[i][m][n]
            removed_indice.append(i)
            continue
        
        #loop over columns
        for j in range(5):
            win = True
            for k in range(5):
                if markeds[i][k][j] == 0 :
                    win = False
                    break
            if win == True:
                break
        if win == True:
            for m in range(5):
                for n in range(5):
                    if markeds[i][m][n] == 0:
                        sum_of_unmarked += boards[win_board][m][n]
            removed_indice.append(i)
            continue

    # drop win boards
    count = 0
    for index in removed_indice:
        boards.pop(index - count)
        markeds.pop(index - count)
        count += 1
        
    return (win, sum_of_unmarked, num, boards, markeds)


# preprocess data
random_nums = getRandomNumbers('random.txt')
boards = getBoards('input.txt')

# initialize numbers for calculation
markeds = []

for i in range(len(boards)):
    markeds.append(np.zeros(shape=(5,5), dtype='int32'))
    
win=False 
i = 0
last_win_sum_of_unmarked, last_win_last_called = 0, 0

while (i<len(random_nums)) & (len(boards)>0):
    markeds = markNumber(random_nums[i], boards, markeds)
    win, sum_of_unmarked, last_called, boards, markeds  = anyWin(random_nums[i], boards, markeds)
    if win == True:
        last_win_sum_of_unmarked, last_win_last_called = sum_of_unmarked, last_called
        win = False
    i += 1

print(last_win_last_called)
print(last_win_sum_of_unmarked)
print(last_win_sum_of_unmarked * last_win_last_called)

