# 백준 2805
import sys
import math
input = sys.stdin.readline

answer = 0
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
S = sum(lst)
for i in range(len(lst)):
    answer = max(answer, math.floor((S-M)//(len(lst)-i)))
    S -= lst[i]
print(answer)
