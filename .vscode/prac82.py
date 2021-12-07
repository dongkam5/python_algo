#백준 9465

for T in range(int(input())):
    n=int(input())
    dp=[[0]*(n+1) for i in range(2)] 
                                   
    row1=list(map(int,input().split()))
    row2=list(map(int,input().split()))
    dp[0][1]=row1[0]
    dp[1][1]=row2[0]

    for i in range(2,n+1):
        dp[0][i]=max(dp[0][i-2]+row1[i-1]+row2[i-2],dp[1][i-2]+row1[i-1],dp[0][i-1])
        dp[1][i]=max(dp[1][i-2]+row2[i-1]+row1[i-2],dp[0][i-2]+row2[i-1],dp[1][i-1])
    
    print(max(max(dp[0]),max(dp[1])))