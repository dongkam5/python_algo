#백준 5557
import sys
input=sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))
dp=[[0]*(21) for _ in range(n)]
dp[0][lst[0]]=1
for i in range(1,n-1):
    for j in range(21):
        if dp[i-1][j]!=0:
            if lst[i]+j<=20:
                dp[i][lst[i]+j]+=dp[i-1][j]
            else:
                dp[i]
            if j-lst[i]>=0:
                dp[i][j-lst[i]]+=dp[i-1][j]

print(dp[n-2][lst[n-1]])