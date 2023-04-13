#프로그래머스 level2 무인도 여행 파이썬

dr=[0,0,1,-1] # dr, dc 를 통해 상하좌우 방향 이동
dc=[1,-1,0,0]

def bfs(start,field):
    q=[]
    cnt=0 # 한 섬의 총 식량을 저장할 변수
    R,C=len(field),len(field[0]) # 행, 열 길이 받음
    start_r,start_c=start #시작점
    visited[start_r][start_c]=int(field[start_r][start_c])
    cnt+=visited[start_r][start_c] 
    q.append((start_r,start_c))
    while q: # 큐가 존재하면 계속 탐색
        r,c=q.pop(0)
        for i in range(4):
            mr=r+dr[i]
            mc=c+dc[i]
            if 0<=mr<R and 0<=mc<C and field[mr][mc]!='X' and visited[mr][mc]==0:
                visited[mr][mc]=visited[r][c]+int(field[mr][mc])
                cnt+=int(field[mr][mc])
                q.append((mr,mc))
    return cnt

def solution(maps):
    answer = []
    field=[]
    R=len(maps)
    C=len(maps[0])
    global visited
    visited=[[0]*C for _ in range(R)] # 방문 확인
    for i in range(R):
        field.append(list(map(str,maps[i])))
    for i in range(R):
        for j in range(C):
            if field[i][j]!='X' and visited[i][j]==0:
                answer.append(bfs((i,j),field))
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]
