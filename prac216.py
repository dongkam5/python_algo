#백준 2468 dfs
import sys
sys.setrecursionlimit(10**6)

dx=[1,-1,0,0]
dy=[0,0,1,-1]
input=sys.stdin.readline
n=int(input())
field=[]
for _ in range(n):
    field.append(list(map(int,input().split())))

def dfs(r,c):
    global ans
    global h
    visit[r][c]=1
    for i in range(4):
        row=r+dy[i]
        col=c+dx[i]
        if 0<=row<n and 0<=col<n and visit[row][col]==0 and field[row][col]>h:
            dfs(row,col)

answer=1
for h in range(1,101):
    visit=[[0]*(n) for _ in range(n)]
    ans=0
    for i in range(n):
        for j in range(n):
            if field[i][j]>h and visit[i][j]==0:
                ans+=1
                dfs(i,j)
    answer=max(answer,ans)

print(answer)