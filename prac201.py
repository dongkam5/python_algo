#백준 15270
import sys
sys.setrecursionlimit(10**6)
N,M=map(int,sys.stdin.readline().split())
link=[[] for _ in range(N+1)]
visit=[0]*(N+1)
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    link[a].append(b)
    link[b].append(a)
    visit[a]=1
    visit[b]=1
def dfs(v):
    global ans
    visit[v]=0
    for i in link[v]:
        if visit[i]==1:
            ans+=1
            dfs(i)
answer=0
for i in range(1,N+1):
    ans=0
    dfs(i)
    ans+=1
    answer+=(ans-ans%2)

if answer==0:
    print(answer+1)
elif (answer+1)<=N:
    print(answer+1)
else:
    print(answer)