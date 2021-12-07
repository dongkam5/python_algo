#백준 1660 못품
import sys
n=int(sys.stdin.readline())
s=[(((i*(i+1)*(2*i+1)+3*i*(i+1))//12)) for i in range(1,121)]
dp=[0]+[10000]*(n)
for i in s:
    if i<=n:
        for k in range(i,n+1):
            dp[k]=min(dp[k],dp[k-i]+1)
    else:
        break
print(dp[n])