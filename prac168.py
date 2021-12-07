#백준 15624
import sys
n=int(sys.stdin.readline())
dp=[0,1]
for i in range(2,n+1):
    dp.append((dp[i-1]+dp[i-2])%1000000007)
print(dp[n])
