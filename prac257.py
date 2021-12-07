#백준 9372
import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    N,M=map(int,input().split())
    graph=[[]*(N+1) for _ in range(N+1)]
    visited=[0]*(N+1)
    for _ in range(M):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    def dfs(idx,cnt):
        visited[idx]=1
        for i in graph[idx]:
            if visited[i]==0:
                cnt=dfs(i,cnt+1)
        return cnt 
    result=dfs(1,0)
    print(result)    