import math

def calErrorScore(line):
    score = 0
    open_chars = ['{', '(', '[', '<']
    close_chars = ['}', ')', ']', '>']
    stack = []
    for char in line:
        stack_size = len(stack)
        if char in close_chars\
                and stack != 0\
                and stack[stack_size - 1] in open_chars:
                    if close_chars.index(char) == open_chars.index(stack[stack_size-1]):
                        stack.pop()
                    else:
                       if char == ')':
                           score += 3
                       elif char == ']':
                           score += 57 
                       elif char == '}':
                           score += 1197
                       elif char == '>':
                           score += 25137
                       return score
        else:
            stack.append(char)

    return score


def isCorrupted(stack):
    close_chars = ['}', ')', ']', '>']
    corrupted = False 
    for char in stack:
        if char in close_chars:
            corrupted = True
            break
    return corrupted
        
    
def calAutoCompleteScore(line):
    score = 0
    open_chars = ['{', '(', '[', '<']
    close_chars = ['}', ')', ']', '>']
    stack = []
    for char in line:
        stack_size = len(stack)
        if char in close_chars\
                and stack_size != 0\
                and stack[stack_size - 1] in open_chars\
                and open_chars.index(stack[stack_size - 1]) == close_chars.index(char):
            stack.pop()
        else:
            stack.append(char)

    corrupted = isCorrupted(stack) 
    if not corrupted:
        stack.reverse()
        for i in range(len(stack)): 
            stack[i] = close_chars[open_chars.index(stack[i])]
            char = stack[i]
            score *=5
            if char == ')':
                score += 1
            elif char == ']':
                score += 2 
            elif char == '}':
                score += 3
            elif char == '>':
                score += 4 

    return score, corrupted



def main():
    with open ('input.txt') as file:
        data = file.read().rstrip('\n')
        lines = data.split("\n")
        total_auto_completion_scores = []
        for line in lines:
            score, corrupted = calAutoCompleteScore(line)
            if not corrupted:
                total_auto_completion_scores.append(score)
        
        middle = math.floor(len(total_auto_completion_scores)/2)
        total_auto_completion_scores.sort()
        print(total_auto_completion_scores[middle])

if __name__ == '__main__':
    main()








