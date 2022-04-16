# 백준 2096 내려가기
import sys
input = sys.stdin.readline
N = int(input())
sel = [-1, 0, 1]
board_M = []
borad_m = []
board_max = list(map(int, input().split()))
board_min = list(map(int, board_max))
for _ in range(1, N):
    board_M = list(map(int, input().split()))
    board_m = list(map(int, board_M))
    for j in range(3):
        M = -1
        m = 1000000
        for k in range(3):
            j_ = j+sel[k]
            if 0 <= j_ < 3:
                M = max(M, board_max[j_])
                m = min(m, board_min[j_])
        board_M[j] += M
        board_m[j] += m
    board_max = list(map(int, board_M))
    board_min = list(map(int, board_m))
print(max(board_max), min(board_min))
