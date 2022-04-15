# 백준 14502 연구소
from collections import deque
import sys
input = sys.stdin.readline
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
R, C = map(int, input().split())
field = []
virus = []
for i in range(R):
    s = list(map(int, input().split()))
    for j in range(C):
        if s[j] == 2:
            virus.append([i, j])
    field.append(s)


def bfs(virus):
    q = deque([])
    for v in virus:
        q.append(v)
    while q:
        r, c = q.popleft()
        for i in range(4):
            n = r+dr[i]
            m = c+dc[i]
            if 0 <= n < R and 0 <= m < C and field_[n][m] == 0:
                field_[n][m] = 2
                q.append([n, m])


answer = 0
point = R*C
for b1 in range(point):
    br1 = b1//C
    bc1 = b1 % C
    if field[br1][bc1] == 0:
        for b2 in range(b1):
            br2 = b2//C
            bc2 = b2 % C
            if field[br2][bc2] == 0:
                for b3 in range(b2):
                    br3 = b3//C
                    bc3 = b3 % C
                    if field[br3][bc3] == 0:
                        field_ = []
                        for i in range(R):
                            field_.append(list(map(int, field[i])))
                        field_[br1][bc1] = 1
                        field_[br2][bc2] = 1
                        field_[br3][bc3] = 1
                        bfs(virus)
                        temp = 0
                        for k in range(R):
                            temp += field_[k].count(0)
                        answer = max(answer, temp)

print(answer)
