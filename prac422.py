# 백준 16928 DFS
import sys
sys.setrecursionlimit = 10**6
N, M = map(int, input().split())
ladder = {}
snake = {}
for _ in range(N):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    snake[a] = b
visited = [100000]*(101)
global answer
answer = 100000


def dfs(num):
    global answer
    if num == 100:
        answer = min(answer, visited[num])
    if num in ladder:
        if visited[ladder[num]] > visited[num]:
            visited[ladder[num]] = visited[num]
            dfs(ladder[num])
    elif num in snake:
        if visited[snake[num]] > visited[num]:
            visited[snake[num]] = visited[num]
            dfs(snake[num])
    else:
        for i in range(6, 0, -1):
            if num+i <= 100:
                if visited[num+i] > visited[num]+1:
                    visited[num+i] = visited[num]+1
                    dfs(num+i)


visited[1] = 0
dfs(1)
print(answer)
