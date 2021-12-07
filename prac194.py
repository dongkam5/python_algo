#프로그래머스 N문제 못품

def solution(N, number):
    answer = 0
    dp=[99999]*(10000000)
    dp[0]=0
    dp[N]=1
    dp[N*11]=2
    dp[N*111]=3
    dp[N*1111]=4
    dp[N*11111]=5
    dp[N*111111]=6
    dp[N*1111111]=7
    for i in range(1,N):
        dp[i]=min(dp[i],dp[i*N]+1,dp[i+N]+1,dp[i+1]+2)
    for i in range(N,number+1):
        dp[i]=min(dp[i],dp[i-N]+1,dp[i//N]+1,dp[i-1]+2)
    for i in range(1,N):
        dp[i]=min(dp[i],dp[i*N]+1,dp[i+N]+1,dp[i+1]+2)
    for i in range(N,number+1):
        dp[i]=min(dp[i],dp[i-N]+1,dp[i//N]+1,dp[i-1]+2)

    answer=dp[number]
    if answer>8:
        answer=-1
    return answer
'''a,b=map(int,input().split())
print(solution(a,b))'''