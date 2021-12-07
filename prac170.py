#백준 19621
import sys
n=int(sys.stdin.readline())
lst=[]
for i in range(n):
    s=list(map(int,sys.stdin.readline().split()))
    lst.append(s)
dp=[0]*(n+1)
if n==1:
    dp[0]=lst[0][2]
    print (dp[0])
elif n==2:
    dp[0]=lst[0][2]
    dp[1]=max(lst[0][2],lst[1][2])
    print (dp[1])
else:
    dp[0]=lst[0][2]
    dp[1]=max(lst[0][2],lst[1][2])
    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2]+lst[i][2])
    print(max(dp))