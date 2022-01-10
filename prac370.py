#프로그래머스 도둑질
def solution(money):
    answer = 0
    dp=[0]*(len(money))
    dp[0]=money[0]
    dp[1]=money[1]
    dp[2]=money[2]+money[0]
    for i in range(3,len(money)-1):
        dp[i]=money[i]+max(dp[i-2],dp[i-3])
    answer=max(dp)
    dp=[0]*(len(money))
    dp[1]=money[1]
    dp[2]=money[2]
    for i in range(3,len(money)):
        dp[i]=money[i]+max(dp[i-2],dp[i-3])
    answer=max(max(dp),answer)
    return answer
