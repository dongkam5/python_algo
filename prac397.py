# 백준 7576
from collections import deque
import sys
input = sys.stdin.readline
answer = 0
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
M, N = map(int, input().split())
box = []
tomatos = deque([])
for i in range(N):
    box.append(list(map(int, input().split())))
    for j in range(M):
        if box[i][j] == 1:
            tomatos.append([i, j])


def bfs():
    while tomatos:
        row, col = tomatos.popleft()
        for i in range(4):
            r, c = row+dr[i], col+dc[i]
            if 0 <= r < N and 0 <= c < M:
                if box[r][c] == 0:
                    box[r][c] = box[row][col]+1
                    tomatos.append([r, c])


bfs()
check = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            check = 1
        answer = max(answer, box[i][j])
if check == 1:
    print(-1)
else:
    print(answer-1)
