#백준 2583 dfs
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
dx=[1,-1,0,0]
dy=[0,0,1,-1]
R,C,K=map(int,input().split())
field=[[0]*(C) for _ in range(R)]

for _ in range(K):
    sc,sr,ec,er=map(int,input().split())
    for i in range(sr,er):
        for j in range(sc,ec):
            field[i][j]=1

def dfs(r,c):
    global ans
    field[r][c]=1
    ans+=1
    for i in range(4):
        q=r+dy[i]
        s=c+dx[i]
        if 0<=q<R and 0<=s<C and field[q][s]==0:
            dfs(q,s)
lst=[]
count=0
for i in range(R):
    for j in range(C):
        if field[i][j]==0:
            ans=0
            count+=1
            dfs(i,j)
            lst.append(ans)

print(count)
lst.sort()
for i in lst:
    print(i,end=' ')
