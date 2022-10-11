# 백준 9012 괄호
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    check = 0
    lst = list(map(str, input().rstrip()))
    # print(lst)
    stack = []
    for val in lst:
        if val == '(':
            stack.append('(')
        else:
            if not stack:
                check = 1
                break
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    check = 1
                    break
    if stack:
        check = 1
    if check == 1:
        print('NO')
    else:
        print('YES')
