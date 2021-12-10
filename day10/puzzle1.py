def isCorrupted(stack):
    close_chars = ['}', ')', ']', '>']
    corrupted = False 
    for char in stack:
        if char in close_chars:
            corrupted = True
            break
    return corrupted
        
    

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

def main():
    with open ('input.txt') as file:
        data = file.read().rstrip('\n')
        lines = data.split("\n")
        total_error_score = 0
        for line in lines:
            total_error_score += calErrorScore(line)
        print(total_error_score)

if __name__ == '__main__':
    main()








