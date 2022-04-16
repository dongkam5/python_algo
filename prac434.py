# 백준 13549 숨바꼭질3
from collections import deque
import re
N, K = map(int, input().split())
visited = [1000000]*(100001)


def bfs(pos):
    q = deque([])
    visited[pos] = 0
    if pos == K:
        return 0
    q.append(pos)
    while q:
        pos = q.popleft()
        jump = pos*2
        back = pos-1
        front = pos+1
        if 0 <= jump <= 100000 and visited[jump] > visited[pos]+1:
            visited[jump] = visited[pos]
            if jump == K:
                return visited[jump]
            q.append(jump)
        if 0 <= back <= 100000 and visited[back] > visited[pos]+1:
            visited[back] = visited[pos]+1
            if back == K:
                return visited[back]
            q.append(back)
        if 0 <= front <= 100000 and visited[front] > visited[pos]+1:
            visited[front] = visited[pos]+1
            if front == K:
                return visited[front]
            q.append(front)


print(bfs(N))
