# 백준 6593 상범 빌딩
from collections import deque
dr = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
dl = [0, 0, 0, 0, 1, -1]


def bfs(start, end):
    visited = [[[10**6]*(C) for _ in range(R)] for _ in range(L)]
    sl, sr, sc = start
    el, er, ec = end
    visited[sl][sr][sc] = 0
    q = deque()
    q.append(start)
    while q:
        pos = q.popleft()
        l, r, c = map(int, pos)
        for i in range(6):
            TL = l+dl[i]
            TC = c+dc[i]
            TR = r+dr[i]
            if 0 <= TL < L and 0 <= TR < R and 0 <= TC < C:
                if field[TL][TR][TC] != '#' and visited[TL][TR][TC] > visited[l][r][c]+1:
                    visited[TL][TR][TC] = visited[l][r][c]+1
                    q.append([TL, TR, TC])
    # print(visited)
    return visited[el][er][ec]


while True:
    L, R, C = map(int, input().split())
    if [L, R, C] == [0, 0, 0]:
        break
    field = []
    for k in range(L):
        temp = []
        for j in range(R):
            s = list(map(str, input()))
            for i in range(C):
                if s[i] == 'S':
                    spos = [k, j, i]
                if s[i] == 'E':
                    epos = [k, j, i]
            temp.append(s)
        if k < L-1:
            n = input()
        field.append(temp)
    ans = bfs(spos, epos)
    if ans == 10**6:
        print('Trapped!')
    else:
        print('Escaped in {} minute(s).'.format(ans))
    n = input()
