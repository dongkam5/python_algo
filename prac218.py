#백준 1926 dfs
import sys
sys.setrecursionlimit(10**6)
dx=[1,-1,0,0]
dy=[0,0,1,-1]
R,C=map(int,sys.stdin.readline().split())
field=[]
for _ in range(R):
    field.append(list(map(int,sys.stdin.readline().split())))

def dfs(r,c):
    global ans
    field[r][c]=0
    ans+=1
    for i in range(4):
        q=r+dy[i]
        s=c+dx[i]
        if 0<=q<R and 0<=s<C and field[q][s]==1:
            dfs(q,s)

count=0
answer=0
for i in range(R):
    for j in range(C):
        if field[i][j]==1:
            count+=1
            ans=0
            dfs(i,j)
            answer=max(ans,answer)

print(count)
print(answer)