# 백준 11000 강의실 배정
import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: x[1])
answer = 0
j = 2
for i in range(N):
    j -= 1
    if j < 1:
        j = 1
    while i+j < N:
        if lst[i+j][0] >= lst[i][1]:
            break
        j += 1
    answer = max(answer, j)
print(answer)
