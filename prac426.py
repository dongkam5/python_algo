# 백준 7569 pypy3 통과
from collections import deque
import sys
dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]
dh = [1, -1]
input = sys.stdin.readline
M, N, H = map(int, input().split())
field = [[[0]*(M) for _ in range(N)] for _ in range(H)]
tomatos = []
for k in range(H):
    for j in range(N):
        s = list(map(int, input().split()))
        for i in range(M):
            if s[i] == 1:
                tomatos.append([k, j, i])
            field[k][j][i] = s[i]


def bfs(tomatos):
    q = deque([])
    for tomato in tomatos:
        q.append(tomato)
    while q:
        pos = q.popleft()
        for i in range(4):
            m = pos[2]+dc[i]
            n = pos[1]+dr[i]
            if 0 <= m < M and 0 <= n < N and field[pos[0]][n][m] != -1 and (field[pos[0]][n][m] == 0 or field[pos[0]][n][m] > 1+field[pos[0]][pos[1]][pos[2]]):
                field[pos[0]][n][m] = 1+field[pos[0]][pos[1]][pos[2]]
                q.append([pos[0], n, m])
        for i in range(2):
            h = pos[0]+dh[i]
            if 0 <= h < H and field[h][pos[1]][pos[2]] != -1 and (field[h][pos[1]][pos[2]] == 0 or field[h][pos[1]][pos[2]] > 1+field[pos[0]][pos[1]][pos[2]]):
                field[h][pos[1]][pos[2]] = 1+field[pos[0]][pos[1]][pos[2]]
                q.append([h, pos[1], pos[2]])


bfs(tomatos)
answer = 0
check = 0
for k in range(H):
    for j in range(N):
        for i in range(M):
            if field[k][j][i] == 0:
                check = 1
                break
            else:
                answer = max(answer, field[k][j][i])
        if check == 1:
            break
    if check == 1:
        break

if check == 1:
    print(-1)
else:
    print(answer-1)
