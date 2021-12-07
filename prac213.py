#백준 21736 dfs
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
R,C=map(int,input().split())
field=[[0]*(C) for _ in range(R)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]
doyeon_r=-1
doyeon_c=-1
for i in range(R):
    s=list(map(str,input().rstrip()))
    for j in range(C):
        if s[j]=='O':
            field[i][j]=1
        elif s[j]=='P':
            field[i][j]=2
        elif s[j]=='I':
            doyeon_r=i
            doyeon_c=j

def dfs(r,c):
    global ans
    if field[r][c]==2:
        ans+=1
    field[r][c]=0
    for i in range(4):
        q=r+dy[i]
        s=c+dx[i]
        if 0<=q<R and 0<=s<C and field[q][s]>0:
            dfs(q,s)

ans=0
dfs(doyeon_r,doyeon_c)
if ans>0:
    print(ans)
else:
    print('TT')