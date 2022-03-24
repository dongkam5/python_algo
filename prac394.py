# 백준 2473 못품
import sys
import itertools
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
val = {}
permu = itertools.combinations(lst, 3)
temp = 1000000001
for p in permu:
    s = sum(p)
    val[s] = p

for key in val.keys():
    if abs(key) < temp:
        temp = abs(key)
        answer = val[key]
answer = list(answer)
answer.sort()
print(*answer)
