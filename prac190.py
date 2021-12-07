#프로그래머스 정수 삼각형
def solution(triangle):
    answer = 0
    n=len(triangle[-1])
    dp=[[0]*(k) for k in range(1,n+1)]
    dp[0][0]=triangle[0][0]
    for i in range(1,n):
        dp[i][0]+=(triangle[i][0]+dp[i-1][0])
        dp[i][-1]+=(triangle[i][-1]+dp[i-1][-1])
        for j in range(1,len(triangle[i])-1):   
            dp[i][j]=max(dp[i][j],dp[i-1][j-1]+triangle[i][j],dp[i-1][j]+triangle[i][j])
    
    answer=max((dp[n-1]))
    return answer

