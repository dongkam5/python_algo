# 백준 9019 DSLR
from collections import deque
import sys
input = sys.stdin.readline


def bfs(start, end):
    q = deque([])
    q.append((start, ''))
    move = ''
    while q:
        start, move = q.popleft()
        D = (start*2) % 10000
        if D == end:
            return move+'D'
        elif visited[D] == 0:
            visited[D] = 1
            q.append((D, move+'D'))

        S = 9999 if start == 0 else start-1
        if S == end:
            return move+'S'
        elif visited[S] == 0:
            visited[S] = 1
            q.append((S, move+'S'))

        L = (start % 1000)*10+start // 1000
        if L == end:
            return move+'L'
        elif visited[L] == 0:
            visited[L] = 1
            q.append((L, move+'L'))
        R = (start % 10)*1000+start//10
        if R == end:
            return move+'R'
        elif visited[R] == 0:
            visited[R] = 1
            q.append((R, move+'R'))


for _ in range(int(input())):
    start, end = map(int, input().split())
    visited = [0]*(10000)
    answer = bfs(start, end)
    print(answer)
