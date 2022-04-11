# 프로그래머스 거스름돈

def solution(n, money):
    answer = 0
    dp = [0]*(1000001)
    for m in money:
        dp[m] = 1
    for i in range(1, 100001):
        k = 0
        for m in money:
            if i > m:
                dp[i] += dp[i-m]*dp[m]
            else:
                break
    print(dp[:n+1])
    return answer


print(solution(5, [1, 2, 5]))
