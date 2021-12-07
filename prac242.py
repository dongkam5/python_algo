#백준 2156 dp
import sys
input=sys.stdin.readline
n=int(input())
lst=[0]*(10001)
for i in range(n):
    lst[i]=int(input())
dp=[0]*(10001)
dp[0]=lst[0]
dp[1]=(lst[0]+lst[1])
dp[2]=max(lst[2]+max(lst[1],lst[0]),dp[1])
for i in range(3,n):
    dp[i]=max(lst[i]+lst[i-1]+dp[i-3],lst[i]+dp[i-2],dp[i-1])
        
print(dp[n-1])