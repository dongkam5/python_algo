#백준 2644 dfs
import sys
sys.setrecursionlimit(10**6)
n=int(sys.stdin.readline())
a,b=map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
visit=[0]*(n+1)
for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    visit[u]=1
    visit[v]=1
ans=0
check=0
answer=0
def dfs(v):
    global check
    global ans
    global answer
    visit[v]=0
    if v==b:
        answer=ans
    if graph[v]:
        for i in graph[v]:
            if visit[i]==1:
                ans+=1
                dfs(i)
        if check==0:
            ans-=1
dfs(a)

if visit[b]==1:
    print(-1)
else:
    print(answer)