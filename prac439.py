# 백준 1753 최단경로
from collections import deque
import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
link = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, cost = map(int, input().split())
    heapq.heappush(link[a], (cost, b))
cost = [10**7]*(V+1)
cost[K] = 0


def search(K):
    q = deque([])
    q.append(K)
    while q:
        node = q.popleft()
        for c, val in link[node]:
            if cost[val] > cost[node]+c:
                cost[val] = cost[node]+c
                q.append(val)


search(K)
for i in range(1, V+1):
    if cost[i] == 10**7:
        print('INF')
    else:
        print(cost[i])
