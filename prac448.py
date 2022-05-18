# 백준 1504 특정한 최단 경로
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
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


v1, v2 = map(int, input().split())
distance_start = dijkstra(graph, 1)
distance_v1 = dijkstra(graph, v1)
distance_v2 = dijkstra(graph, v2)

answer = float('inf')
v1_v2 = distance_start[v1]+distance_v1[v2]+distance_v2[N]
v2_v1 = distance_start[v2]+distance_v2[v1]+distance_v1[N]
answer = min(answer, v1_v2, v2_v1)
if answer == float('inf'):
    print(-1)
else:
    print(answer)
