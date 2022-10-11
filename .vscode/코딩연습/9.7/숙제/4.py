# 백준 1874 스택 수열
import sys
input = sys.stdin.readline
N = int(input())
num = 0
stack = []
ans = []
check = 0
for _ in range(N):
    k = int(input())
    if num < k:
        for _ in range(num, k):
            ans.append('+')
            num += 1
            stack.append(num)
        stack.pop()
        ans.append('-')
    elif stack and k >= stack[-1]:
        while True:
            val = stack[-1]
            if val == k:
                stack.pop()
                ans.append('-')
                break
            elif val > k:
                stack.pop()
                ans.append('-')
            else:
                check = 1
                break
    else:
        check = 1
if check == 1:
    print('NO')
else:
    for a in ans:
        print(a)
