# 프로그래머스 가장 먼노드 bfs

from collections import deque


def solution(n, edge):
    answer = 0
    visited = [0]*(n+1)
    cnt = [0]*(n+1)
    link = [[] for _ in range(n+1)]
    for e in edge:
        a, b = e
        link[a].append(b)
        link[b].append(a)

    def bfs(node, count_):
        q = deque([])
        q.append([node, count_])
        while q:
            node, count_ = q.popleft()
            for next_node in link[node]:
                if visited[next_node] == 0:
                    visited[next_node] = 1
                    q.append([next_node, count_+1])
                    cnt[next_node] = count_+1
        M = max(cnt)
        return cnt.count(M)
    visited[1] = 1
    answer = bfs(1, 0)
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
