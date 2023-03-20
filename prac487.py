#백준 1389 케빈 베이컨 게임
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
network=[[] for _ in range(N+1)] # 각 사람당 연결된 사람을 저장하기 위한 이중 리스트 생성
answer_cnt=10**9
answer_pnum=10**9
for _ in range(M): #서로 네트워크에 추가
    a,b=map(int,input().split())
    network[a].append(b) 
    network[b].append(a)

for startnum in range(1,N+1): #bfs를 이용
    visited=[0]*(N+1) #방문값 0으로 초기화
    total=0 # 케빈 베이컨 값의 합을 저장할 total
    cnt=0   # 시작점부터 각 요소까지의 케빈 베이컨 값을 저장할 cnt
    q=[]
    visited[startnum]=1
    q.append([startnum,cnt])
    while q:
        pnum,cnt=q.pop(0) #큐에서 맨 앞 값을 빼냄
        total+=cnt
        for person in network[pnum]: #연결된 사람 들 중 
            if visited[person]==0: # 방문하지 않았으면
                visited[person]=1 #방문했다고 visted를 갱신
                q.append([person,cnt+1]) #연결된 사람과 케빈 베이컨 값 전달
    if total<answer_cnt: #케빈 베이컨 값의 합이 작으면
        answer_cnt=total #케빈 베이컨 값의 합 갱신
        answer_pnum=startnum #시작 사람 갱신
    elif total==answer_cnt:
        if startnum<answer_pnum:
            answer_pnum=startnum

print(answer_pnum)