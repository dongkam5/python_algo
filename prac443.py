# 백준 5972 택배배송
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
    distance = {node: float('inf') for node in range(1, N+1)}
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [distance[start], start])
    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        if distance[current_destination] < current_distance:
            continue
        for new_destination, new_distance in graph[current_destination]:
            dist = new_distance+current_distance
            if dist < distance[new_destination]:
                distance[new_destination] = dist
                heapq.heappush(queue, [dist, new_destination])
    return distance


distance = dijkstra(graph, 1)
print(distance[N])
