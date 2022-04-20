# 백준 1377 버블 소트
import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
lst = {}
lst_sorted = []
lst_val = []
answer = -1
diffs = defaultdict(lambda: 1000001)
for i in range(N):
    K = int(input())
    lst[K] = i
    lst_sorted.append(K)
lst_sorted.sort()
for i in range(N):
    diff = min(abs(lst[lst_sorted[i]]-i), N-i-1)
    diffs[lst_sorted[i]] = min(diffs[lst_sorted[i]], diff)

for diff in diffs.values():
    answer = max(answer, diff)
print(answer+1)
