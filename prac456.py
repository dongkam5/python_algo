# 백준 2636 치즈
from collections import deque
import sys
input = sys.stdin.readline
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
N, M = map(int, input().split())
field = []
cheese_cnt = 0
for _ in range(N):
    s = list(map(int, input().split()))
    for val in s:
        if val == 1:
            cheese_cnt += 1
    field.append(s)


def bfs(start):
    start_r, start_c = start
    visited[start_r][start_c] = 1
    q = deque([])
    q.append((start_r, start_c))
    while q:
        curr_r, curr_c = q.popleft()
        for k in range(4):
            R = curr_r+dr[k]
            C = curr_c+dc[k]
            if 0 <= R < N and 0 <= C < M and visited[R][C] == 0:
                if field[R][C] == 1:
                    visited[R][C] = 1
                    del_lst.append((R, C))
                elif field[R][C] == 0:
                    visited[R][C] = 1
                    q.append((R, C))


cnt = 0
while True:
    if cheese_cnt == 0:
        break
    visited = [[0]*(M) for _ in range(N)]
    del_lst = []
    for i in range(N):
        if field[i][0] == 0 and visited[i][0] == 0:
            bfs((i, 0))
    for i in range(N):
        if field[i][M-1] == 0 and visited[i][M-1] == 0:
            bfs((i, M-1))
    for j in range(M):
        if field[0][j] == 0 and visited[0][j] == 0:
            bfs((0, j))
    for j in range(M):
        if field[N-1][j] == 0 and visited[N-1][j] == 0:
            bfs((N-1, j))

    del_cnt = len(del_lst)
    for del_pos in del_lst:
        r, c = del_pos
        field[r][c] = 0
    cheese_cnt -= del_cnt
    cnt += 1
print(cnt)
print(del_cnt)
