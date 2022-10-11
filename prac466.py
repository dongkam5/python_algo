# 백준 5014 스타트링크
from collections import deque
F, S, G, U, D = map(int, input().split())


def bfs(F, S, G, U, D):
    visited = [10**6]*(F+1)
    visited[S] = 0
    q = deque()
    q.append(S)
    while q:
        pos = q.popleft()
        if pos+U <= F and visited[pos+U] > visited[pos]+1:
            visited[pos+U] = visited[pos]+1
            q.append(pos+U)
        if pos-D >= 1 and visited[pos-D] > visited[pos]+1:
            visited[pos-D] = visited[pos]+1
            q.append(pos-D)
    # print(visited)
    return visited[G]


ans = bfs(F, S, G, U, D)
if ans == 10**6:
    print('use the stairs')
else:
    print(ans)
