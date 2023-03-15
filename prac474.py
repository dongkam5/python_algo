#프로그래머스 level1 바탕화면 정리
def solution(wallpaper):
    answer = []
    R=len(wallpaper)
    C=len(wallpaper[0])
    left=C
    right=0
    up=R
    down=0
    for i in range(R):
        for j in range(C):
            if wallpaper[i][j]=='#':
                if left>j:
                    left=j
                if right<j:
                    right=j
                if up>i:
                    up=i
                if down<i:
                    down=i
    answer=[up,left,down+1,right+1]
    return answer