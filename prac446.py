# 백준 11909 배열 탈출
import sys
input = sys.stdin.readline
N = int(input())
field = []
val = [[10**6]*(N) for _ in range(N)]
for _ in range(N):
    field.append(list(map(int, input().split())))
val[0][0] = 0

for i in range(N):
    for j in range(N):
        down = i-1
        left = j-1
        if down >= 0:
            if field[down][j] > field[i][j]:
                val[i][j] = min(val[i][j], val[down][j])
            else:
                diff = field[i][j]-field[down][j]
                val[i][j] = min(val[i][j], diff+1+val[down][j])
        if left >= 0:
            if field[i][left] > field[i][j]:
                val[i][j] = min(val[i][j], val[i][left])
            else:
                diff = field[i][j]-field[i][left]
                val[i][j] = min(val[i][j], diff+1+val[i][left])
print(val[N-1][N-1])
