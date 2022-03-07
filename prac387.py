# 백준 4949
import sys
input = sys.stdin.readline
while True:
    line = input().rstrip()
    stack = []
    if len(line) == 1 and line[0] == '.':
        break
    else:
        check = 0
        for i in range(len(line)):
            if line[i] == '(' or line[i] == '[':
                stack.append(line[i])
            elif line[i] == ')':
                if stack:
                    comp = stack.pop()
                    if comp != '(':
                        check = 1
                        break
                else:
                    check = 1
                    break
            elif line[i] == ']':
                if stack:
                    comp = stack.pop()
                    if comp != '[':
                        check = 1
                        break
                else:
                    check = 1
                    break
        if check == 0 and not stack:
            print('yes')
        else:
            print('no')
