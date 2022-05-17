# 백준 17396 백도어
import queue
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
N, M = map(int, input().split())
permission = list(map(int, input().split()))
permission[N-1] = 0
graph = defaultdict(list)
for _ in range(M):
    a, b, cost = map(int, input().split())
    if permission[a] == 0 and permission[b] == 0:
        graph[a].append([b, cost])
        graph[b].append([a, cost])


def dijkstra(graph, start):
    distances = {node: float('inf') for node in range(N)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        curr_dist, curr_destination = heapq.heappop(queue)
        if distances[curr_destination] < curr_dist:
            continue
        for new_destination, new_dist in graph[curr_destination]:
            dist = new_dist+curr_dist
            if dist < distances[new_destination]:
                distances[new_destination] = dist
                heapq.heappush(queue, [dist, new_destination])
    return distances


distances = dijkstra(graph, 0)
if distances[N-1] == float('inf'):
    print(-1)
else:
    print(distances[N-1])
