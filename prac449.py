# 백준 14503 로봇 청소기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N, M = map(int, input().split())
curr_r, curr_c, direc = map(int, input().split())
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))
visited = [[0]*(M) for _ in range(N)]


def search(row, col, direc, cnt, stack):
    if stack == 4:
        back_r = row+dr[(direc-2) % 4]
        back_c = col+dc[(direc-2) % 4]
        if field[back_r][back_c] == 1:
            print(cnt)
            return
        elif field[back_r][back_c] == 0:
            stack = 0
            search(back_r, back_c, direc, cnt, stack)
    else:
        direc -= 1
        R = row+dr[direc % 4]
        C = col+dc[direc % 4]
        if visited[R][C] == 0 and field[R][C] == 0:
            stack = 0
            visited[R][C] = 1
            cnt += 1
            search(R, C, direc, cnt, stack)
        else:
            stack += 1
            search(row, col, direc, cnt, stack)


cnt = 1
stack = 0
direc += 10000
visited[curr_r][curr_c] = 1
search(curr_r, curr_c, direc, cnt, stack)
