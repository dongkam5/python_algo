# 백준 1377 버블 소트
import sys
input = sys.stdin.readline
N = int(input())
lst = {}
lst_sorted = []
lst_val = []
answer = -1
for i in range(N):
    K = int(input())
    lst[K] = i
    lst_sorted.append(K)
lst_sorted.sort()
print()
for i in range(N):
    if lst[lst_sorted[i]]-i >= 0:
        diff = min(lst[lst_sorted[i]]-i, N-i-1)
    else:
        diff = N-i
    print(diff)
    answer = max(diff, answer)
print(answer+1)
