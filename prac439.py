# 백준 1753 최단경로
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)
for _ in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])


def dijkstra(graph, start):
    distances = {node: float('INF') for node in range(1, V+1)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance+new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances


distances = dijkstra(graph, K)
for val in distances.values():
    if val == float('inf'):
        print('INF')
    else:
        print(val)
