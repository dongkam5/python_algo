# 백준 2493 맞춤
import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
answer = [0]*(n)
stack = []
for i in range(len(lst)):
    if not stack:
        stack.append([lst[i], i, 0])
    else:
        if stack[-1][0] <= lst[i]:
            while stack and stack[-1][0] <= lst[i]:
                val = stack.pop()
                answer[val[1]] = val[2]
        if stack:
            stack.append([lst[i], i, stack[-1][1]+1])
        else:
            stack.append([lst[i], i, 0])

while stack:
    val = stack.pop()
    answer[val[1]] = val[2]
print(*answer)
'''
# 백준 2493 오답
import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
dp = [0]*(n)

for i in range(n):
    for j in range(i+1, n):
        if lst[i] < lst[j]:
            break
        elif lst[i] == lst[j]:
            dp[j] = (i+1)
            break
        else:
            dp[j] = (i+1)

print(*dp)
'''
