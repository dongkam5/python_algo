#백준 5525 IOIOI
import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
S=list(map(str,input().rstrip()))
target=2*N+1
dp=[0]*(M)
answer=0

if S[0]=='I':
    dp[0]=1

for i in range(1,M):
    prev=S[i-1]
    now=S[i]
    if S[i]==S[i-1]:
        if S[i]=='I':
            dp[i]=1
        else:
            dp[i]=0
    else:
        dp[i]=dp[i-1]+1

for i in range(M):
    if dp[i]>=target and dp[i]%2==1:
        answer+=1
print(answer)