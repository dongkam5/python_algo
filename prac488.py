#백준 2178 미로 탐색
import sys
input=sys.stdin.readline
dr=[1,0,-1,0] #위 아래
dc=[0,-1,0,1] # 좌 우
N,M=map(int,input().split())
maze=[]
for _ in range(N):
    maze.append(list(map(int,input().rstrip()))) # 미로 값 저장

def bfs(start,maze):
    visited=[[0]*M for _ in range(N)] #방문 값을 0으로 초기화
    start_r,start_c=start #시작 행,렬 받음
    visited[start_r][start_c]=1 # 시작 행 렬을 1로 초기화
    q=[]
    q.append([start_r,start_c]) #큐에 추가
    while q:
        r,c=q.pop(0) #큐에서 뺌
        if r==N-1 and c==M-1: #도착하면
            return visited[r][c] #최종 거리를 리턴
        for i in range(4): #상하좌우로 탐색
            R=r+dr[i]
            C=c+dc[i]
            if 0<=R<N and 0<=C<M and maze[R][C]==1 and visited[R][C]==0: #미로 안에 있는지 탐색 & 갈 수 있는 길인지 & 방문했는지 탐색
                visited[R][C]=visited[r][c]+1 #거리를 갱신 (visted 이용)
                q.append([R,C]) #큐에 추가
        # for val in visited:
        #     print(val)
        # print()

ans=bfs([0,0],maze)
print(ans)
