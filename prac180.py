#백준 1912
import sys
n=int(sys.stdin.readline())
s=list(map(int,sys.stdin.readline().split()))
dp=[-1001]*(n)
dp[0]=s[0]
for i in range(1,n):
        dp[i]=max(s[i],dp[i-1]+s[i])

print(max(dp))