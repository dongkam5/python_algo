n,m=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
s=[]
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in lst:
        s.append(i)
        dfs()
        s.pop()

dfs()