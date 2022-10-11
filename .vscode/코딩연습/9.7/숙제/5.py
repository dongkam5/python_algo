# 백준 2504 괄호의 값
import sys
input = sys.stdin.readline
lst = list(map(str, input().rstrip()))
stack = []
ans = 0
temp = 1
for i in range(len(lst)):
    if lst[i] == '(':
        stack.append(lst[i])
        temp *= 2
    elif lst[i] == '[':
        stack.append(lst[i])
        temp *= 3
    elif lst[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if lst[i-1] == '(':
            ans += temp
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if lst[i-1] == '[':
            ans += temp
        stack.pop()
        temp //= 3
if stack:
    print(0)
else:
    print(ans)
