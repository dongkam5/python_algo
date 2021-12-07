#11724

import sys
sys.setrecursionlimit(10000)
n,m=map(int,input().split())
s=[[0]*(n+1) for i in range(n+1)]
visit=[0 for i in range(n+1)]
check=0

def dfs(v):
    visit[v]=1
    for i in range(1,n+1):
        if visit[i]==0 and s[v][i]==1:
            dfs(i)
for i in range(m):
    x,y=map(int,input().split())
    s[x][y]=1
    s[y][x]=1


for i in range(1,n+1):
    if visit[i]==0:
        dfs(i)
        check+=1

print(check)