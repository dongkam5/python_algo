#14606
n=int(input())

dp=[0]*(n+1)

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i]=dp[i//2]+dp[i-i//2]+(i//2)*(i-i//2)
print(dp[n])