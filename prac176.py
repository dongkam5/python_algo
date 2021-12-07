#백준 1965
n=int(input())
lst=list(map(int,input().split()))
dp=[1]*(n+1)
for i in range(1,n):
    for j in range(0,i):
        if lst[i]>lst[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))