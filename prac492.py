#백준 11403 경로 찾기
import sys
input=sys.stdin.readline
N=int(input())
graph=[[]*N for _ in range(N)] #방향 그래프를 저장할 이중 리스트 새성
for i in range(N):
    s=list(map(int,input().split())) #각 행에 대해서
    for j in range(N):
        if s[j]==1: #i,j로 갈 수 있는 지 확인
            graph[i].append(j) # 그래프에 추가
answer=[[0]*N for _ in range(N)] #정답을 반환할 이중 리스트 생성

def bfs(start_node):
    visited=[0]*(N) #방문했는지 확인하기 위한 리스트
    q=[]
    q.append(start_node) #시작노드 큐에 추가
    while q:
        node=q.pop(0) #큐에서 제일 앞 노드를 빼냄
        for next_node in graph[node]:
            if visited[next_node]==0: #방문 하지 않았다면
                visited[next_node]=1 #방문으로 갱신
                answer[start_node][next_node]=1 #start_node 에서 next_node로 갈 수 있다고 정답 리스트 값 갱신
                q.append(next_node) #큐에 노드 추가

for i in range(N): #각 노드(i)에 대해서 bfs!
    bfs(i)
for i in range(N):
    for j in range(N):
        if j==N-1:
            print(answer[i][j])
        else:
            print(answer[i][j],end=' ')