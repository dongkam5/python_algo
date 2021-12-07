#프로그래머스 거리두기 확인하기
def solution(places):
    answer = []
    dx=[0,2,0,-2]
    dy=[2,0,-2,0]
    for place in places:
        lst=[['0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0']]
        for i in place:
            s=list(map(str,i))
            s.insert(0,'0')
            s.insert(0,'0')
            s.insert(7,'0')
            s.insert(7,'0')
            lst.append(s)
        lst.append(['0','0','0','0','0','0','0','0','0'])
        lst.append(['0','0','0','0','0','0','0','0','0'])
        check=1
        for i in range(2,7):
            for j in range(2,7):
                if lst[i][j]=='P':
                    for d in range(4):
                        n=i+dy[d]//2
                        m=j+dx[d]//2
                        if lst[n][m]=='P':
                            check=0
                            break
                    for d in range(4):
                        n=i+dy[d]
                        m=j+dx[d]
                        if lst[n][m]=='P' and (lst[i+dy[d]//2][j+dx[d]//2]=='O'):
                            check=0
                            break
                    if lst[i+1][j+1]=='P' and (lst[i+1][j]=='O' or lst[i][j+1]=='O'):
                        check=0
                    if lst[i+1][j-1]=='P' and (lst[i+1][j]=='O' or lst[i][j-1]=='O'):
                        check=0
                    if lst[i-1][j+1]=='P' and (lst[i-1][j]=='O' or lst[i][j+1]=='O'):
                        check=0
                    if lst[i-1][j-1]=='P' and (lst[i-1][j]=='O' or lst[i][j-1]=='O'):
                        check=0
                if check==0:
                    break
            if check==0:
                break       
        answer.append(check)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))