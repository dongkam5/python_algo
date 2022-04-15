# 백준 14500 테트로미노
import sys
sys.setrecursionlimit = 10**6
input = sys.stdin.readline
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
N, M = map(int, input().split())
field = []
visited = [[0]*(M) for _ in range(N)]
global answer
answer = 0
for i in range(N):
    field.append(list(map(int, input().split())))


def dfs(r, c, cnt, val):
    global answer
    if cnt >= 4:
        answer = max(answer, val)
        return
    else:
        for i in range(4):
            s = r+dr[i]
            q = c+dc[i]
            if 0 <= s < N and 0 <= q < M:
                if visited[s][q] == 0:
                    visited[s][q] = 1
                    dfs(s, q, cnt+1, val+field[s][q])
                    visited[s][q] = 0


def checkone(r, c):
    global answer
    for i in range(4):
        val = field[r][c]
        for j in range(4):
            if i != j:
                s = r+dr[j]
                q = c+dc[j]
                if 0 <= s < N and 0 <= q < M:
                    val += field[s][q]
                else:
                    val = 0
                    break
        answer = max(val, answer)


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, field[i][j])
        visited[i][j] = 0
        checkone(i, j)

print(answer)
