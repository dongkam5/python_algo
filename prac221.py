#백준 11123 dfs
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(r,c):
    global ans
    field[r][c]='.'
    ans+=1
    for i in range(4):
        q=r+dy[i]
        s=c+dx[i]
        if 0<=q<R and 0<=s<C and field[q][s]=='#':
            dfs(q,s)

for _ in range(int(input())):
    R,C=map(int,input().split())
    field=[]
    for _ in range(R):
        field.append(list(map(str,input().rstrip())))
    
    count=0
    for i in range(R):
        for j in range(C):
            if field[i][j]=='#':
                ans=0
                dfs(i,j)
                count+=1
    print(count)