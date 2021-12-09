#프로그래머스 방문 길이

def solution(dirs):
    answer = 0
    link=[[[[0]*11 for _ in range(11)] for _ in range(11)] for _ in range(11)]
    x=5
    y=5
    for dir in dirs:
        if dir=='U' and y<10:
            if (link[x][y][x][y+1]!=1) and (link[x][y+1][x][y]!=1):
                answer+=1
            link[x][y][x][y+1]=1
            link[x][y+1][x][y]=1
            y+=1
        elif dir=='D' and y>0:
            if (link[x][y][x][y-1]!=1) and (link[x][y-1][x][y]!=1):
                answer+=1
            link[x][y][x][y-1]=1
            link[x][y-1][x][y]=1
            y-=1
        elif dir=='L' and x>0:
            if (link[x][y][x-1][y]!=1) and (link[x-1][y][x][y]!=1):
                answer+=1
            link[x][y][x-1][y]=1
            link[x-1][y][x][y]=1
            x-=1
        elif dir=='R' and x<10:
            if (link[x][y][x+1][y]!=1) and (link[x+1][y][x][y]!=1):
                answer+=1
            link[x][y][x+1][y]=1
            link[x+1][y][x][y]=1
            x+=1
    return answer

print(solution('ULUR'))