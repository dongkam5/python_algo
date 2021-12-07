#백준 1743 dfs
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
dx=[1,-1,0,0]
dy=[0,0,1,-1]
R,C,K=map(int,input().split())
field=[[0]*(C) for _ in range(R)]
for _ in range(K):
    r,c=map(int,input().split())
    field[r-1][c-1]=1

def dfs(r,c):
    global ans
    field[r][c]=0
    ans+=1
    for i in range(4):
        q=r+dy[i]
        s=c+dx[i]
        if 0<=q<R and 0<=s<C and field[q][s]==1:
            dfs(q,s)
answer=0
for i in range(R):
    for j in range(C):
        if field[i][j]==1:
            ans=0
            dfs(i,j)
            answer=max(answer,ans)
print(answer)