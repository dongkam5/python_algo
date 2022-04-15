# 백준 2206 벽 부수고 이동하기
from collections import deque
import sys
input = sys.stdin.readline
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
N, M = map(int, input().split())
field = []
wall = deque([])
for i in range(N):
    field.append(list(map(int, input().rstrip())))


def bfs(r, c):
    q = deque([])
    q.append([r, c])
    while q:
        r, c = q.popleft()
        for i in range(4):
            r_ = r+dr[i]
            c_ = c+dc[i]
            if 0 <= r_ < N and 0 <= c_ < M and field_[r_][c_] == 0:
                field_[r_][c_] = field_[r][c]+1
                q.append([r_, c_])


def bfscheck(r, c):
    q = deque([])
    q.append([r, c])
    while q:
        r, c = q.popleft()
        for i in range(4):
            r_ = r+dr[i]
            c_ = c+dc[i]
            if 0 <= r_ < N and 0 <= c_ < M:
                if field_[r_][c_] == 0:
                    field_[r_][c_] = field_[r][c]+1
                    q.append([r_, c_])
                elif field_[r_][c_] == 1:
                    wall.append([r_, c_])


answer = 10000
field_ = []
for k in range(N):
    field_.append(list(map(int, field[k])))
bfscheck(0, 0)

for w in wall:
    field_ = []
    i, j = w
    for k in range(N):
        field_.append(list(map(int, field[k])))
    field_[i][j] = 0
    bfs(0, 0)
    if field_[N-1][M-1] != 0:
        answer = min(answer, field_[N-1][M-1])

if answer == 10000:
    print(-1)
else:
    print(answer+1)
