#프로그래머스 level2 숫자 변환하기
def solution(x, y, n):
    answer = 0
    dp=[10**6]*(y+1)
    dp[y]=0
    for i in range(y,x-1,-1):
        if i%2==0:
            dp[i//2]=min(dp[i]+1,dp[i//2])
        if i%3==0:
            dp[i//3]=min(dp[i]+1,dp[i//3])
        dp[i-n]=min(dp[i]+1,dp[i-n])
    if dp[x]==10**6:
        answer=-1
    else:
        answer=dp[x]
    return answer
