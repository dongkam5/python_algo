# 백준 1068 트리
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
root = 0
del_num = int(input())
tree = [[] for _ in range(N)]
for i in range(N):
    if lst[i] == -1:
        root = i
    else:
        if i != del_num:
            tree[lst[i]].append(i)


def bfs(start, del_num):
    answer = 0
    visited = [0]*(N)
    visited[del_num] = 1
    q = deque([])
    q.append(start)
    while q:
        node = q.popleft()
        if visited[node] == 0 and len(tree[node]) != 0:
            visited[node] = 1
            for next_node in tree[node]:
                if visited[next_node] == 0:
                    q.append(next_node)
        elif visited[node] == 0 and len(tree[node]) == 0:
            answer += 1
    return answer


ans = bfs(root, del_num)
# print(tree)
print(ans)
