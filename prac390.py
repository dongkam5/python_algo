# 백준 1987
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
R, C = map(int, input().split())
move = [[0, 1], [1, 0], [-1, 0], [0, -1]]
global answer
answer = 0
field = []
for _ in range(R):
    field.append(list(map(str, input().rstrip())))
visit = {}
for i in range(26):
    visit[chr(i+65)] = 0


def dfs(r, c, cnt):
    global answer
    cnt += 1
    visit[field[r][c]] = 1
    answer = max(answer, cnt)
    for i in range(4):
        q, s = move[i][0], move[i][1]
        if 0 <= (r+q) < R and 0 <= (c+s) < C:
            if visit[field[r+q][c+s]] == 0:
                dfs(r+q, c+s, cnt)
    cnt -= 1
    visit[field[r][c]] = 0


dfs(0, 0, 0)

print(answer)
