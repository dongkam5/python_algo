#백준 9507
import sys
n=int(sys.stdin.readline())
dp=[1,1,2,4]
for i in range(4,70):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4])
for _ in range(n):
    k=int(sys.stdin.readline())
    print(dp[k])