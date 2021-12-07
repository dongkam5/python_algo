#1759
L,C=map(int,input().split())
lst=list(map(str,input().split()))
lst.sort()
s=[]
def dfs():
    if len(s)==L:
        check=0
        for i in s:
            if ((i=='a')or(i=='e')or(i=='i')or(i=='o')or(i=='u')):
                check+=1
        if check>=1 and (len(s)-check)>=2:
            print(''.join(map(str,s)))
        check=0
        return
    for i in lst:
        if len(s)==0:
            s.append(i)
            dfs()
            s.pop()
        else:
            if s[len(s)-1]>=i:
                pass
            else:   
                s.append(i)
                dfs()
                s.pop()

dfs()