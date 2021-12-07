#백준 14002
import sys
n=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
dp=[0]*(n)
s=[[] for _ in range(n)]
for i in range(n):
    for j in range(i):
        if lst[i]>lst[j] and dp[i]<dp[j]:
             dp[i]=dp[j]
             s[i]=list(map(int,s[j]))
    dp[i]+=1
    s[i].append(lst[i])
print(max(dp))
for i in (s[dp.index(max(dp))]):
    print(i,end=' ')