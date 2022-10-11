# 백준 9084 동전
import sys
input = sys.stdin.readline


def dp(lst, goal):
    l = [0]*(goal+1)
    for val in lst:
        l[val] = 1
    for i in range(1, goal+1):
        for val in lst:
            if i-val >= 0:
                l[i] = max(l[i], l[i-val]+1)
    return l[goal]


for _ in range(int(input().rstrip())):
    N = int(input())
    lst = list(map(int, input().split()))
    goal = int(input())
    ans = dp(lst, goal)
    print(ans)
