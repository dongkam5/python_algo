# 백준 14284 간선 이어가기2
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])


def dijkstra(graph, start):
    distances = {node: float('inf') for node in range(1, N+1)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        curr_dist, curr_dest = heapq.heappop(queue)
        if distances[curr_dest] < curr_dist:
            continue
        for new_dest, new_dist in graph[curr_dest]:
            dist = curr_dist+new_dist
            if dist < distances[new_dest]:
                distances[new_dest] = dist
                heapq.heappush(queue, [dist, new_dest])
    return distances


start, end = map(int, input().split())
distances = dijkstra(graph, start)
print(distances[end])
