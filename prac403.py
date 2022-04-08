# 프로그래머스 N으로 표현

def solution(N, number):
    answer = 0
    dp = [10000]*(1000000)
    for i in range(1, 7):
        s = str(N)*i
        dp[int(s)] = i
    for i in range(2, 100000):
        if i > N:
            dp[i] = min(dp[i], dp[i*N]+1, dp[i+N] + 1, dp[i-N]+1,)
        else:
            dp[i] = min(dp[i], dp[i*N]+1, dp[i+N]+1)
    answer = dp[number]
    if answer >= 8:
        answer = -1
    return answer


print(solution(9, 8))
