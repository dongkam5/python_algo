#백준 13565 dfs
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
R,C=map(int,input().split())
field=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for _ in range(R):
    field.append(list(map(int,input().rstrip())))
def dfs(r,c):
    global ans
    if r==R-1 and field[r][c]==0:
        ans+=1
        return
    field[r][c]=1
    for i in range(4):
        q=r+dy[i]
        s=c+dx[i]
        if 0<=q<R and 0<=s<C and field[q][s]==0:
            dfs(q,s)
ans=0
for i in range(C):
    if field[0][i]==0:
        dfs(0,i)
        if ans>=1:
            break
if ans>=1:
    print('YES')
else:
    print('NO')