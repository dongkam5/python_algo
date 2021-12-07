#백준 1890
import sys
input=sys.stdin.readline
n=int(input())
field=[]
for _ in range(n):
    field.append(list(map(int,input().split())))
dp=[[0]*(n) for _ in range(n)]
dp[0][0]=1

for i in range(n):
    for j in range(n):
        move=field[i][j]
        if i==n-1 and j==n-1:
            continue
        if (move+i)<n:
            dp[i+move][j]+=dp[i][j]
        if (move+j)<n:
            dp[i][j+move]+=dp[i][j]

print(dp[n-1][n-1])