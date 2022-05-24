# 백준 2636 치즈
import sys
input = sys.stdin.readline
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
N, M = map(int, input().split())
field = []
cheese_cnt = 0
answer = 0
for _ in range(N):
    s = list(map(int, input().split()))
    for val in s:
        if val == 1:
            cheese_cnt += 1
    field.append(s)
cnt = 0
while True:
    del_pos = []
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                for k in range(4):
                    R = i+dr[k]
                    C = j+dc[k]
                    if 0 <= R < N and 0 <= C < M:
                        if field[R][C] == 1:
                            continue
                        else:
                            del_pos.append((i, j))
                            cheese_cnt -= 1
                            break
                    else:
                        continue
    if del_pos:
        cnt += 1
        if cheese_cnt == 0:
            print(del_pos)
            answer = len(del_pos)
            break
        for pos in del_pos:
            r, c = pos
            field[r][c] = 0
    else:
        break
print(cnt)
print(answer)
