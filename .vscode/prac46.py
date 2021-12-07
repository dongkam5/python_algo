#15655
n,m=map(int,input().split())

lst=list(map(int,input().split()))
lst.sort()
s=[]
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in lst:
        if i in s :
            continue
        if len(s)==0:
            s.append(i)
            dfs()
            s.pop()
        elif s[len(s)-1]<i:
            s.append(i)
            dfs()
            s.pop()

dfs()

