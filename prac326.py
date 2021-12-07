#프로그래머스 게임 맵 최단거리 dfs (안됨)
def solution(maps):
    import sys
    sys.setrecursionlimit(10**6)
    global answer
    global ans
    answer = 10000
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    M=len(maps[0])
    N=len(maps)
    visit=[[0]*(M) for _ in range(N)]
    ans=1
    def dfs(n,m):
        global ans
        global answer
        if n==N-1 and m==M-1:
            answer=min(answer,ans)
            return
        for i in range(4):
            q=dx[i]+m
            s=dy[i]+n
            if  N>s>=0 and M>q>=0 and visit[s][q]==0 and maps[s][q]==1:
                visit[s][q]=1
                ans+=1
                dfs(s,q)
                visit[s][q]=0
                ans-=1
    visit[0][0]=1
    dfs(0,0)
    if answer==10000:
        answer=-1
        return answer
    else:
        return answer

print(solution([[1]]))
print(solution([[1],[1],[1]]))
