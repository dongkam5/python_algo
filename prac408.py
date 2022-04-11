# 프로그래머스 2 x n 타일링

def solution(n):
    answer = 0
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (2*dp[i-1]+dp[i-2]) % 1000000007
    answer = dp[n]
    return answer
