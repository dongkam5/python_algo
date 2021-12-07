#백준 3187 dfs
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
R,C=map(int,input().split())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
field=[[0]*(250) for _ in range(250)]
for i in range(R):
    s=list(map(str,sys.stdin.readline()))
    for j in range(C):
        if s[j]=='.':
            field[i][j]=1
        elif s[j]=='v':
            field[i][j]=2
        elif s[j]=='k':
            field[i][j]=3

def dfs(r,c):
    global l
    global w
    if field[r][c]==2:
        w+=1
    elif field[r][c]==3:
        l+=1
    field[r][c]=0
    for i in range(4):
        q=r+dy[i]
        s=c+dx[i]
        if 0<=q<R and 0<=s<C and field[q][s]>0:
            dfs(q,s)
lamb=0
wolf=0
for i in range(R):
    for j in range(C):
        if field[i][j]>0:
            l=0
            w=0
            dfs(i,j)
            if l>w:
                lamb+=l
            else:
                wolf+=w

print(lamb,wolf)