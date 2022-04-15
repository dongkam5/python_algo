# 백준 16928 BFS
from collections import deque
import sys
N, M = map(int, input().split())
ladder = {}
snake = {}
for _ in range(N):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    snake[a] = b
visited = [0]*(101)
global answer
answer = 100000
visited = [10000]*(101)


def bfs(num):
    global answer
    q = deque([])
    q.append(num)
    while q:
        num = q.popleft()
        if num == 100:
            answer = visited[100]
        else:
            if num in ladder:
                if visited[ladder[num]] > visited[num]:
                    visited[ladder[num]] = visited[num]
                    q.append(ladder[num])
            elif num in snake:
                if visited[snake[num]] > visited[num]:
                    visited[snake[num]] = visited[num]
                    q.append(snake[num])
            else:
                for i in range(6, 0, -1):
                    if num+i <= 100:
                        if visited[num+i] > visited[num]+1:
                            visited[num+i] = visited[num]+1
                            q.append(num+i)


visited[1] = 0
bfs(1)
print(answer)
