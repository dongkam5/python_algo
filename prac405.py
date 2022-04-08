# 프로그래머스 가장 먼노드 실패코드 dfs

def solution(n, edge):
    answer = 0
    visited = [0]*(n+1)
    cnt = [10000]*(n+1)
    link = [[] for _ in range(n+1)]
    for e in edge:
        a, b = e
        link[a].append(b)
        link[b].append(a)
    cnt[1] = 0

    def serach_dfs(node, count_):
        cnt[int(node)] = min(cnt[node], count_)
        if link[node]:
            for next_node in link[node]:
                if visited[next_node] == 0:
                    visited[next_node] = 1
                    serach_dfs(next_node, count_+1)
                    visited[next_node] = 0
    serach_dfs(1, 0)
    cnt.pop(0)
    M = max(cnt)
    answer = cnt.count(M)
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
