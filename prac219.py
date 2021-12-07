#백준 14716 dfs
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
dx=[1,-1,0,0,1,1,-1,-1]
dy=[0,0,1,-1,1,-1,1,-1]
R,C=map(int,input().split())
field=[]
for _ in range(R):
    field.append(list(map(int,input().split())))

def dfs(r,c):
    field[r][c]=0
    for i in range(8):
        q=r+dy[i]
        s=c+dx[i]
        if 0<=q<R and 0<=s<C and field[q][s]==1:
            dfs(q,s)
count=0
for i in range(R):
    for j in range(C):
        if field[i][j]==1:
            count+=1
            dfs(i,j)

print(count)
