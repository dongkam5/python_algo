#백준 17291 이상한 문제(오류같음)
n=int(input())
dp=[0,1,2,4,7]
for i in range(5,21):
    if i%2==0:
        dp.append(dp[i-1]*2-dp[i-4]-dp[i-5])
    else:
        dp.append(dp[i-1]*2)

print(dp[n])
