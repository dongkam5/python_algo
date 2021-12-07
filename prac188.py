#백준 18249
import sys
n=int(sys.stdin.readline())
dp=[0]*(191230)
dp[1]=1
dp[2]=2
for i in range(3,191230):
    dp[i]=((dp[i-1]+dp[i-2])%1000000007)
for _ in range(n):
    k=int(sys.stdin.readline())
    print(dp[k])