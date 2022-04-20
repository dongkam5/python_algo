# 백준 16236 아기상어
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
field = []
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
fish_cnt = 0
answer = 0
level = 2
result = 1
cnt = 0


for i in range(N):
    s = list(map(int, input().split()))
    for j in range(N):
        if s[j] == 9:
            pos = [i, j]
        elif 0 < s[j] <= 6:
            fish_cnt += 1
    field.append(list(map(int, s)))


def bfs(pos, level):
    visited = [[0]*(N) for _ in range(N)]
    q = deque([])
    q.append(pos)
    fishes = []
    min_dist = 10**6
    while q:
        r, c = q.popleft()
        for i in range(4):
            R = r+dr[i]
            C = c+dc[i]
            if 0 <= R < N and 0 <= C < N and not visited[R][C]:
                visited[R][C] = visited[r][c]+1
                if 0 < field[R][C] < level:
                    min_dist = visited[R][C]
                    fishes.append([visited[R][C], R, C])
                elif field[R][C] == level and min_dist >= visited[R][C]:
                    q.append([R, C])
                elif field[R][C] == 0 and min_dist >= visited[R][C]:
                    q.append([R, C])
    if fishes:
        fishes.sort()
        return fishes[0]
    else:
        return False


while fish_cnt:
    result = bfs(pos, level)
    if result:
        cnt += 1
        pos_r, pos_c = pos
        field[pos_r][pos_c] = 0
        dist, result_r, result_c = result
        answer += dist
        field[result_r][result_c] = 999
        pos = [result_r, result_c]
        fish_cnt -= 1
        if cnt == level:
            cnt = 0
            level += 1
    else:
        break

print(answer)
