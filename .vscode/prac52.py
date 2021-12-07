#6603
while(True):
    lst=list(map(int,input().split()))
    k=lst.pop(0)
    s=[]
    if k==0:
        break
    def dfs():
        if len(s)==6:
            print(' '.join(map(str,s)))
            return
        for i in lst:
            if len(s)==0:
                s.append(i)
                dfs()
                s.pop()
            elif s[len(s)-1]<i:
                s.append(i)
                dfs()
                s.pop()
    dfs()
    print()