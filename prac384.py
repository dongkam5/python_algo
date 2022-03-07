# 백준 1018
N, M = map(int, input().split())
field = []
answer = 10000000
w_row = 'WBWBWBWB'
b_row = 'BWBWBWBW'
for _ in range(N):
    field.append(list(map(str, input())))
for i in range(N-7):
    for j in range(M-7):
        f_diff = 0
        s_diff = 0
        for k in range(i, i+8):
            row = field[k][j:j+8]
            for v in range(8):
                if k % 2 == 0:
                    if w_row[v] != row[v]:
                        f_diff += 1
                    if b_row[v] != row[v]:
                        s_diff += 1
                else:
                    if b_row[v] != row[v]:
                        f_diff += 1
                    if w_row[v] != row[v]:
                        s_diff += 1
        answer = min(answer, f_diff, s_diff)
print(answer)
