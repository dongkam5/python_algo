#백준 16174 dfs
import sys
sys.setrecursionlimit(4100)
n=int(sys.stdin.readline())
field=[]
for _ in range(n):
    field.append(list(map(int,sys.stdin.readline().split())))
visit=[[0]*(n) for _ in range(n)]
def dfs(r,c):
    global check
    visit[r][c]=1
    move=field[r][c]
    if r==n-1 and c==n-1:
        check=1
        print('HaruHaru')
        quit()
    if move!=0:
        if r+move<n and visit[r+move][c]==0:
            dfs(r+move,c)
        if c+move<n and visit[r][c+move]==0:
            dfs(r,c+move)

check=0
dfs(0,0)
if check==0:
    print('Hing')