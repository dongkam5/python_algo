#백준 11724 dfs
import sys
sys.setrecursionlimit(10**6)
N,M=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
visited=[0]*(N+1)
lst=[]
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    lst.append(a)
    lst.append(b)
    visited[a]=1
    visited[b]=1
def dfs(graph,s):
    visited[s]=0
    for i in graph[s]:
        if visited[i]==1:
            visited[i]=0
            dfs(graph,i)

ans=0
for i in range(N):    
    if visited[i]==1:
        ans+=1
        dfs(graph,i)

print(N-len(set(lst))+ans)