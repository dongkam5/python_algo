# 백준 2251 물통
import sys
sys.setrecursionlimit(10**6)
A, B, C = map(int, input().split())
visited = [[0]*(201) for _ in range(3)]
ans = []


def search(a, b, c):
    global A, B, C
    if not (visited[0][a] == 1 and visited[1][b] == 1 and visited[2][c] == 1):
        if a == 0:
            ans.append(c)
        visited[0][a] = 1
        visited[1][b] = 1
        visited[2][c] = 1
        if a != 0:
            temp = a+b
            if temp <= B:
                search(0, temp, c)
            else:
                search(temp-B, B, c)
            temp = a+c
            if temp <= C:
                search(0, b, temp)
            else:
                search(temp-C, b, C)
        if b != 0:
            temp = a+b
            if temp <= A:
                search(temp, 0, c)
            else:
                search(A, temp-A, c)
            temp = b+c
            if temp <= C:
                search(a, 0, temp)
            else:
                search(a, temp-C, C)
        if c != 0:
            temp = a+c
            if temp <= A:
                search(temp, b, 0)
            else:
                search(A, b, temp-A)
            temp = b+c
            if temp <= B:
                search(a, temp, 0)
            else:
                search(a, B, temp-B)


search(0, 0, C)


ans = list(set(ans))
ans.sort()
print(*ans)
