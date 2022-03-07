# 백준 10816
import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
field = [0]*(20000001)
for value in lst:
    field[value+10000000] += 1
M = int(input())
search = list(map(int, input().split()))
for value in search:
    print(field[value+10000000], end=' ')
