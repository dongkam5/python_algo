#백준 4796
import sys
i=1
while True:
    L,P,V=map(int,sys.stdin.readline().split())
    ans=0
    if L==0 and P==0 and V==0:
        break
    else:
        m=(V//P)
        ans+=m*L+min(V-(m*P),L)
    print('Case {}: {}'.format(i,ans))
    i+=1
