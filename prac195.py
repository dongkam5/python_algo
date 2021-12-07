#백준 2293
import sys
n,k=map(int,sys.stdin.readline().split())
lst=[]
for i in range(n):
    lst.append(int(sys.stdin.readline()))
dp=[0]*(k+1)
for i in range(k,-1,-1):
    for j in lst:
        if i+j<=k:
            dp[i]=max(dp[i],dp[i+j]+1)

print(dp[0])