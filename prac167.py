#백준 14495
import sys
n=int(sys.stdin.readline())
dp=[0,1,1,1]
for i in range(4,120):
    dp.append(dp[i-1]+dp[i-3])
print(dp[n])