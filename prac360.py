#백준 9251 LCS
import sys
input=sys.stdin.readline
f=list(map(str,input().rstrip()))
s=list(map(str,input().rstrip()))
f_len=len(f)
s_len=len(s)
dp=[[0]*(s_len+1) for _ in range(f_len+1)]

for i in range(1,f_len+1):
    for j in range(1,s_len+1):
        if f[i-1]==s[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])