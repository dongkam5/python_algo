#백준 17204 그래프
import sys
input=sys.stdin.readline
N,K=map(int,input().split())
visited=[0]*(N)
def dfs(i,cnt):
    global check
    if i==K:
        check=1
        print(cnt)
        return
    visited[i]=1
    if visited[link[i]]==0:
        dfs(link[i],cnt+1)
link=[0]*(N)
for i in range(N):
    a=int(input())
    link[i]=a
check=0
dfs(0,0)
if check==0:
    print(-1)
