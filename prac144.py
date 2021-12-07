#백준 9009
import sys
dp=[0]*(101)
dp[0]=0
dp[1]=1
dp[2]=1
dp[3]=2
for i in range(3,51):
    dp[i]=dp[i-1]+dp[i-2]
n=int(sys.stdin.readline())
for i in range(n):
    ans=[]
    k=int(sys.stdin.readline())
    for j in range(50,0,-1):
        if k>=dp[j]:
            k-=dp[j]
            ans.append(dp[j])
        if k==0:
            break
    ans.sort()
    for a in ans:
        print(a,end=' ')
    print()
