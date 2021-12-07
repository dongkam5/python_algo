#백준 14248 bfs
import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))
start=int(input())
visit=[0]*(n)
def bfs(s):
    q=deque()
    q.append(s)
    while q:
        s=q.popleft()
        visit[s]=1
        r=s+lst[s]
        l=s-lst[s]
        if 0<=r<n and visit[r]==0:
            q.append(r)
        if 0<=l<n and visit[l]==0:
            q.append(l)
bfs(start-1)
print(visit.count(1))
'''#백준 14248 dfs
import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))
start=int(input())
visit=[0]*(n)
def dfs(s):
    visit[s]=1
    r=s+lst[s]
    l=s-lst[s]
    if 0<=r<n and visit[r]==0:
        dfs(r)
    if 0<=l<n and visit[l]==0:
        dfs(l)
dfs(start-1)
print(visit.count(1))'''