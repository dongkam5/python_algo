#프로그래머스 배달 dfs
def solution(N, road, K):
    answer = 0
    visited=[0]*(N+1)
    link=[[] for _ in range(N+1)]
    for r in road:
        a,b,cost=map(int,r)
        link[a].append([b,cost])
        link[b].append([a,cost])
    lst={}
    def dfs(node,cost):
        visited[node]=1
        if cost<=K:
            lst[node]=1
            for i in range(len(link[node])):
                if visited[link[node][i][0]]==0:
                    dfs(link[node][i][0],cost+link[node][i][1])
        visited[node]=0
    dfs(1,0)
    answer=len(lst)
    return answer
