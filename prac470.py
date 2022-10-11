# 백준 9084 동전
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    goal = int(input())
    dp = [0]*(goal+1)
    for val in lst:
        dp[val] = 1
    for i in range(1, goal+1):
        for j in range(len(lst)-1, -1, -1):
            if i >= lst[j] and dp[i] == 0:
                dp[i] += (dp[i-lst[j]]+1)
    print(dp[goal])
