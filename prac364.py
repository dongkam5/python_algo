#프로그래머스 배달 bfs
def solution(N, road, K):
    answer = 0
    from collections import deque
    link=[[] for _ in range(N+1)]
    visit=[500001]*(N+1)
    for r in road:
            a,b,cost=map(int,r)
            link[a].append([b,cost])
            link[b].append([a,cost])
    lst={}
    def bfs(node,cost):
        q=deque([])
        q.append((node,cost))
        while q:
            n,c=q.popleft()
            visit[n]=c
            if c<=K:
                lst[n]=1
                for i in range(len(link[n])):
                    if visit[link[n][i][0]]>(c+link[n][i][1]):
                        visit[link[n][i][0]]=(c+link[n][i][1])
                        q.append((link[n][i][0],(c+link[n][i][1])))
    bfs(1,0)
    answer=len(lst)
    return answer