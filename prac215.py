#백준 2667
import sys
sys.setrecursionlimit(10**6)
dx=[1,-1,0,0]
dy=[0,0,1,-1]
input=sys.stdin.readline
n=int(input())
field=[]
for _ in range(n):
    field.append(list(map(int,input().rstrip())))
def dfs(r,c):
    global ans
    field[r][c]=0
    ans+=1
    for i in range(4):
        row=r+dy[i]
        col=c+dx[i]
        if 0<=row<n and 0<=col<n and field[row][col]==1:
            dfs(row,col)
answer=[]
for i in range(n):
    for j in range(n):
        if field[i][j]==1:
            ans=0
            dfs(i,j)
            answer.append(ans)
answer.sort()

print(len(answer))
for i in answer:
    print(i)