#백준 11060
import sys
n=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
dp=[1000]*(n)
dp[0]=0
for i in range(n):
    k=1
    while i+k<=i+lst[i] and i+k<n:
        dp[i+k]=min(dp[i+k],dp[i]+1)
        k+=1
print(-1 if dp[n-1]==1000 else dp[n-1])