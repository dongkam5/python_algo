# 백준 1920
N = int(input())
lst = set(list(map(int, input().split())))
M = int(input())
search = list(map(int, input().split()))
for val in search:
    if val in lst:
        print(1)
    else:
        print(0)
