#백준 9461
import sys
T=int(sys.stdin.readline())
dp=[0,1,1,1]
for i in range(4,101):
    dp.append(dp[i-2]+dp[i-3])
for i in range(T):
    n=int(sys.stdin.readline())
    print(dp[n])