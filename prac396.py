# 백준 1987
import sys
input = sys.stdin.readline
R, C = map(int, input().split())
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
field = []
for _ in range(R):
    field.append(list(map(str, input().rstrip())))
visit = [0]*(26)
answer = 0


def dfs(r, c, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        row, col = r+dr[i], c+dc[i]
        if 0 <= row < R and 0 <= col < C and visit[ord(field[row][col])-65] == 0:
            visit[ord(field[row][col])-65] = 1
            dfs(row, col, cnt+1)
            visit[ord(field[row][col])-65] = 0


visit[ord(field[0][0])-65] = 1
dfs(0, 0, 1)
print(answer)
