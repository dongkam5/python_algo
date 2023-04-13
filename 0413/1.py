#프로그래머스 level2 미로 탈출

dr=[0,0,1,-1]
dc=[1,-1,0,0]

def bfs(start,goal,field):
    q=[]
    R,C=len(field),len(field[0])
    visited=[[0]*C for _ in range(R)]
    start_r,start_c=start
    goal_r,goal_c=goal
    q.append((start_r,start_c))
    while q:
        r,c=q.pop(0)
        if goal_r==r and goal_c==c:
            return visited[r][c]
        for i in range(4):
            mr=r+dr[i]
            mc=c+dc[i]
            if 0<=mr<R and 0<=mc<C and field[mr][mc]!='X' and visited[mr][mc]==0:
                visited[mr][mc]=visited[r][c]+1
                q.append((mr,mc))
    return -1

def solution(maps):
    answer = 0
    field=[]
    R=len(maps)
    C=len(maps[0])
    for i in range(R):
        field.append(list(map(str,maps[i])))
        for j in range(C):
            if maps[i][j]=='S':
                start=(i,j)
            elif maps[i][j]=='L':
                lever=(i,j)
            elif maps[i][j]=='E':
                end=(i,j)
    ans=bfs(start,lever,field)
    if ans==-1:
        return -1
    answer+=ans
    ans=bfs(lever,end,field)
    if ans==-1:
        return -1
    answer+=ans
    return answer
