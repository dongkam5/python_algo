#백준 11725
import sys
sys.setrecursionlimit(10**6)
n=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

ans=[0]*(n+1)
visit=[0]*(n+1)
def dfs(v):
    visit[v]=1
    for i in graph[v]:
        if visit[i]==0:
            ans[i]=v
            dfs(i)

dfs(1)
for i in range(2,n+1):
    print(ans[i])