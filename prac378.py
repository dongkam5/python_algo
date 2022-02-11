# 백준 2166
import sys
input = sys.stdin.readline
n = int(input())
pos = []
for _ in range(n):
    cardi = list(map(int, input().split()))
    pos.append(cardi)
pos.append(pos[0])
answer = 0
for i in range(n):
    answer += (pos[i][0]*pos[i+1][1])
    answer -= (pos[i][1]*pos[i+1][0])

print(round(abs(answer)/2, 1))
