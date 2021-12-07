#백준 2705
import sys
T=int(input())
dp=[0]*(1001)
dp[0]=1
dp[1]=1
dp[2]=2
dp[3]=2
for i in range(4,1001):
    for k in range(1,(i//2)+1):
        dp[i]+=dp[k]
    dp[i]+=1
for _ in range(T):
    n=int(sys.stdin.readline())
    print(dp[n])
