# 백준 10026 적녹색맹
from collections import deque
import sys
input = sys.stdin.readline
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
n = int(input())
field = []
for _ in range(n):
    field.append(list(map(str, input().rstrip())))


def bfs(r, c, lst):
    q = deque([])
    q.append([r, c])
    while q:
        r, c = q.popleft()
        for i in range(4):
            s = r+dr[i]
            w = c+dc[i]
            if 0 <= s < n and 0 <= w < n and field[s][w] not in lst and visited[s][w] == 0:
                visited[s][w] = 1
                q.append([s, w])


R = 0
G = 0
B = 0
RG = 0

mix = 0

# 빨간색 체크
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and field[i][j] == 'R':
            bfs(i, j, ['G', 'B'])
            R += 1

# 파란색 체크
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and field[i][j] == 'B':
            bfs(i, j, ['G', 'R'])
            B += 1

# 초록색 체크
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and field[i][j] == 'G':
            bfs(i, j, ['R', 'B'])
            G += 1

# 적녹 체크
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and (field[i][j] == 'R' or field[i][j] == 'G'):
            bfs(i, j, ['B'])
            RG += 1

print(R+G+B, RG+B)
