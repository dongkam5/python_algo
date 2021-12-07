#백준 13565 bfs
import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,-1,1]
def bfs(r,c):
    q=deque()
    q.append((r,c))
    field[r][c]=2
    while q:
        r,c=q.popleft()
        for i in range(4):
            row=r+dy[i]
            col=c+dx[i]
            if 0<=row<R and 0<=col<C and field[row][col]==0:
                q.append((row,col))
                field[row][col]=2

R,C=map(int,sys.stdin.readline().split())
field=[]
for _ in range(R):
    field.append(list(map(int,sys.stdin.readline().rstrip())))

for i in range(C):
    if field[0][i]==0:
        bfs(0,i)
print('YES' if 2 in field[R-1] else 'NO')