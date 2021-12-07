#프로그래머스 게임 맵 최단거리 bfs (정답)
def solution(maps):
    from collections import deque
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    M=len(maps[0])
    N=len(maps)
    visit=[[0]*(M) for _ in range(N)]
    ans=1
    def bfs(h,w):
        queue=deque([])
        queue.append((0,0))
        while queue:
            n,m=queue.popleft()
            if n==N-1 and m==M-1:
                return visit[N-1][M-1]
            for i in range(4):
                q=dx[i]+m
                s=dy[i]+n
                if  N>s>=0 and M>q>=0 and visit[s][q]==0 and maps[s][q]==1:
                    visit[s][q]=visit[n][m]+1
                    queue.append((s,q))
    visit[0][0]=1
    answer=bfs(0,0)
    if answer:
        return answer
    else:
        return -1
     

print(solution([[1]]))
print(solution([[1],[1],[1]]))
