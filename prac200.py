#백준 1012 dfs
import sys
sys.setrecursionlimit(10000)
dx=[1,-1,0,0]
dy=[0,0,-1,1]
def dfs(checked,y,x):
    checked[y][x]=0
    for i in range(4):
        q=x+dx[i]
        w=y+dy[i]
        if 0<=q<M and 0<=w<N and checked[w][q]:
            dfs(checked,w,q)
    '''if x+1<M and checked[y][x+1]==1:
        check=1
        dfs(checked,y,x+1)
    if 0<=x-1 and checked[y][x-1]==1:
        check=1
        dfs(checked,y,x-1)
    if y+1<N and checked[y+1][x]==1:
        check=1
        dfs(checked,y+1,x)
    if 0<=y-1 and checked[y-1][x]==1:
        check=1
        dfs(checked,y-1,x)
    if check==0:
        return'''
    

for _ in range(int(sys.stdin.readline())):
    M,N,K=map(int,sys.stdin.readline().split())
    checked=[[0]*(M) for _ in range(N)]
    for _ in range(K):
        a,b=map(int,sys.stdin.readline().split())
        checked[b][a]=1
    ans=0
    for y in range(N):
        for x in range(M):
            if checked[y][x]==1:
                ans+=1
                dfs(checked,y,x)

    print(ans)