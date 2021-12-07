#백준 4963
import sys
sys.setrecursionlimit(10**6)
dx=[0,1,1,1,0,-1,-1,-1]
dy=[-1,-1,0,1,1,1,0,-1]
def dfs(field,r,c):
    global w,h
    field[r][c]=0
    for i in range(8):
        q=c+dx[i]
        s=r+dy[i]
        if 0<=q<w and 0<=s<h and field[s][q]==1:
            dfs(field,s,q)
    
while True:
    w,h=map(int,sys.stdin.readline().split())
    if w==0 and h==0:
        break
    field=[]
    for r in range(h):
        field.append(list(map(int,sys.stdin.readline().split())))
    ans=0
    for i in range(h):
        for j in range(w):
            if field[i][j]==1:
                ans+=1
                dfs(field,i,j)
    print(ans)