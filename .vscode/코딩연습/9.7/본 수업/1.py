# 백준 2800 괄호 제거
import sys
from itertools import combinations
input = sys.stdin.readline
lst = list(map(str, input().rstrip()))
stack = []
arr = []
for i in range(len(lst)):
    if lst[i] == '(':
        stack.append(i)
    elif lst[i] == ')':
        k = stack.pop()
        arr.append([k, i])
# arr.sort()
ans = []
for i in range(1, len(lst)+1):
    comb = combinations(arr, i)
    for c in comb:
        sol = ''
        temp = list(map(str, lst))
        for val in c:
            temp[val[0]] = '?'
            temp[val[1]] = '?'
        for val in temp:
            if val != '?':
                sol += val
        ans.append(sol)
ans.sort()
dup = []
for val in ans:
    if not val in dup:
        dup.append(val)
        print(val)
