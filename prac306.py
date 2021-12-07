#프로그래머스 땅따먹기

def solution(land):
    n=len(land)
    m=len(land[0])
    dp=[[0]*(m) for _ in range(n)]
    for i in range(m):
        dp[0][i]=land[0][i]
    for i in range(1,n):
        for j in range(m):
            for k in range(m):
                if j!=k:
                    dp[i][j]=max(dp[i][j],dp[i-1][k]+land[i][j])
    answer = max(dp[n-1])
    return answer


'''다른사람풀이
def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])
'''