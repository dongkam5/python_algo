# 백준 1197 최소 스패닝 트리
from collections import deque
import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
link = []
visited = [0]*(V+1)
for _ in range(E):
    a, b, c = map(int, input().split())
    heapq.heappush(link, [c, a, b])
c, a, b = heapq.heappop(link)
visited[a] = 1
visited[b] = 1
answer = c
cnt = 2
temp = deque([])
while cnt < V:
    while True:
        c, a, b = heapq.heappop(link)
        if visited[a] == 1 and visited[b] == 1:
            continue
        elif visited[a] == 1 and visited[b] == 0:
            visited[b] = 1
            cnt += 1
            answer += c
            break
        elif visited[a] == 0 and visited[b] == 1:
            visited[a] = 1
            cnt += 1
            answer += c
            break
        else:
            temp.append([c, a, b])
    while temp:
        t = temp.popleft()
        heapq.heappush(link, [t[0], t[1], t[2]])

print(answer)
