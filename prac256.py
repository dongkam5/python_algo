#프로그래머스 네트워크
def solution(n, computers):
    import sys
    sys.setrecursionlimit(10**6)
    answer = 0
    visited=[0]*(n)
    def dfs(v):
        visited[v]=1
        for link in range (len(computers[v])):
            if link!=v and computers[v][link]!=0 and visited[link]==0:
                dfs(link)
    for i in range(n):
        if visited[i]==0:
            dfs(i)
            answer+=1
    return answer

solution(3,[[1, 1, 0], [1, 1, 1], [0, 0, 1]])