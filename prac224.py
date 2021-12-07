#백준 13023
import sys
sys.setrecursionlimit(410000)
input=sys.stdin.readline
N,M=map(int,input().split())
link=[[] for _ in range(N)]
visit=[0]*(N)

for i in range(M):
    a,b=map(int,input().split())
    link[a].append(b)
    link[b].append(a)
    visit[a]=1
    visit[b]=1
def dfs(i):
    global ans
    global answer
    visit[i]=0
    if ans>=4:
        answer=ans
        return
    for k in link[i]:
        if visit[k]==1:
            ans+=1
            dfs(k)
            visit[k]=1
            ans-=1
    visit[i]=1
answer=0
for i in range(N):
    if answer>=4:
        break
    if visit[i]==1:
        ans=0
        dfs(i)
if answer>=4:
    print(1)
else:
    print(0)