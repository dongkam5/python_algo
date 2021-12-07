#백준 2606 dfs
import sys
n=int(sys.stdin.readline())
link=int(sys.stdin.readline())

graph=[[] for _ in range(n+1)]
for _ in range(link):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
checked=[0]*(n+1)

def dfs(s):
    checked[s]=1
    for i in graph[s]:
        if checked[i]==0:
            dfs(i)
if link==0:
    print(0)
else:    
    dfs(1)
    print(checked.count(1)-1)

'''다른풀이
n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [0]*(n+1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt +=1
 
dfs(1)
print(cnt)

'''