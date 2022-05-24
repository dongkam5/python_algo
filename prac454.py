# 백준 2589 보물섬
from collections import deque
import sys
input = sys.stdin.readline
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

N, M = map(int, input().split())
field = []
for _ in range(N):
    field.append(list(map(str, input().rstrip())))


def bfs(start):
    dist = 0
    start_r, start_c, start_dist = start
    q = deque([])
    q.append((start_r, start_c, start_dist))
    while q:
        curr_r, curr_c, curr_dist = q.popleft()
        for i in range(4):
            R = curr_r+dr[i]
            C = curr_c+dc[i]
            if 0 <= R < N and 0 <= C < M and field[R][C] == 'L' and visited[R][C] == 0:
                visited[R][C] = 1
                q.append((R, C, curr_dist+1))
                dist = max(dist, curr_dist+1)
    return dist


answer = 0
for i in range(N):
    for j in range(M):
        visited = [[0]*(M) for _ in range(N)]
        if field[i][j] == 'L':
            visited[i][j] = 1
            dist = bfs((i, j, 0))
            answer = max(answer, dist)

print(answer)
