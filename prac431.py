# 백준 15686 치킨배달 pypy3 통과
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
N, M = map(int, input().split())
field = []
cHouses = []
clients = []
for i in range(N):
    s = list(map(int, input().split()))
    for j in range(N):
        if s[j] == 2:
            cHouses.append([i, j])
        elif s[j] == 1:
            clients.append([i, j])
    field.append(list(map(int, s)))


def bfs(combi):
    q = deque([])
    for client in clients:
        r, c = client
        field_[r][c] = 1
    for cHouse in combi:
        r, c = cHouse
        field_[r][c] = 2
        visited[r][c] = 0
        q.append([r, c])
    dist = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            R = r+dr[i]
            C = c+dc[i]
            if 0 <= R < N and 0 <= C < N and visited[R][C] == 0 and [R, C] not in combi:
                visited[R][C] = visited[r][c]+1
                q.append([R, C])
                if field_[R][C] == 1:
                    dist += visited[R][C]
    return dist


lst = []
combination = combinations(cHouses, M)
for combi in combination:
    visited = [[0]*N for _ in range(N)]
    field_ = [[0]*N for _ in range(N)]
    lst.append(bfs(combi))
print(min(lst))
