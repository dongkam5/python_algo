#백준 2294 dp
n,k=map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(int(input()))
dp=[100000]*(k+1)
dp[0]=0

for i in lst:
    for j in range(1,k+1):
        if j-i>=0:
            dp[j]=min(dp[j],dp[j-i]+1)

if dp[k]==100000:
    print(-1)
else:
    print(dp[k])