#백준 10844 dp
n=int(input())
dp=[[0]*(10) for _ in range (101)]

for i in range(10):
    dp[0][i]=1
for i in range(101):
    for j in range(10):
        if j==9:
            dp[i][9]+=((dp[i-1][8]))
        elif j==0:
            dp[i][0]+=(dp[i-1][1])
        else:
            dp[i][j]+=((dp[i-1][j+1]+dp[i-1][j-1]))


print(sum(dp[n-1][1:])%1000000000)