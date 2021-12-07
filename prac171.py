#백준 17175
dp=[1,1,3]
n=int(input())
for i in range(3,51):
    dp.append((dp[i-1]+dp[i-2]+1)%1000000007)

print(dp[n])