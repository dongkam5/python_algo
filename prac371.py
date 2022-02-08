# 프로그래머스 N으로 표현
def solution(N, number):
    answer = 0
    dp=[0]*(32001)
    for i in range(1,32001):
        if i>5:
            dp[i]=min(dp[i-5],dp[i//5]+1+dp[i%5])
    return answer