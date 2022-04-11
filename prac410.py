# 프로그래머스 순위

from collections import deque


def solution(n, results):
    answer = 0
    win = [[] for _ in range(n+1)]
    loss = [[] for _ in range(n+1)]
    win_check = [0]*(n+1)
    loss_check = [0]*(n+1)
    visited = [0]*(n+1)
    for result in results:
        a, b = result
        win[a].append(b)
        loss[b].append(a)

    def win_bfs(node):
        q = deque([])
        q.append(node)
        this_node = node
        cnt = 0
        while q:
            node = q.popleft()
            for next_node in win[node]:
                if visited[next_node] == 0:
                    q.append(next_node)
                    cnt += 1
                    visited[next_node] = 1
                    win_check[this_node] = cnt

    def loss_bfs(node):
        q = deque([])
        q.append(node)
        this_node = node
        cnt = 0
        while q:
            node = q.popleft()
            for next_node in loss[node]:
                if visited[next_node] == 0:
                    q.append(next_node)
                    cnt += 1
                    visited[next_node] = 1
                    loss_check[this_node] = cnt
    for i in range(1, n+1):
        visited = [0]*(n+1)
        win_bfs(i)
        visited = [0]*(n+1)
        loss_bfs(i)
    for i in range(1, n+1):
        if win_check[i]+loss_check[i] == n-1:
            answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
