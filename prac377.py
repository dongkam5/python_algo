# 백준 12852
n = int(input())
dp = [[] for _ in range(n+1)]

for i in range(1, n+1):
    if i % 6 == 0:
        if len(dp[i//3]) <= len(dp[i//2]):
            dp[i] = dp[i//3]+[i]
        else:
            dp[i] = dp[i//2]+[i]
    elif i % 3 == 0:
        if len(dp[i//3]) <= len(dp[i-1]):
            dp[i] = dp[i//3]+[i]
        else:
            dp[i] = dp[i-1]+[i]
    elif i % 2 == 0:
        if len(dp[i//2]) <= len(dp[i-1]):
            dp[i] = dp[i//2]+[i]
        else:
            dp[i] = dp[i-1]+[i]
    else:
        dp[i] = dp[i-1]+[i]

print(len(dp[n])-1)
print(*dp[n][::-1])
