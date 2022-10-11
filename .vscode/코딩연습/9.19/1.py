# 백준 4811 알약
import sys
input = sys.stdin.readline
ans = [0]*(32)
dp = [[0]*32 for _ in range(32)]
for i in range(1, 32):
    dp[i][0] = 1
for i in range(1, 32):
    for j in range(1, i+1):
        dp[j][i] = dp[j-1][i]+dp[j][i-1]
    # dp[j+1][i]=dp[j][i]

while True:
    N = int(input())
    if N == 0:
        break
    print(dp[N+1][N+1])
