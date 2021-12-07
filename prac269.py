#백준 15666
import sys
n,m=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()

d={}
line=[]
def dfs(cnt):
    if cnt==m:
        s=' '.join(map(str,line))
        if s not in d:
            d[s]=1
            print(s)
        return
    for j in range(n):
        if line[-1]<=lst[j]:
            line.append(lst[j])
            dfs(cnt+1)
            line.pop()

for i in range(n):
    line.append(lst[i])
    dfs(1)
    line.pop()
