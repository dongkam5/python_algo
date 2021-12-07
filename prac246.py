#백준 2631 dp
import sys
input=sys.stdin.readline
n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
dp=[1]*(n)

for i in range(n):
    for j in range(i):
        if lst[j]<lst[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))