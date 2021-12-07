#코드포스 C
import sys
from collections import deque
input=sys.stdin.readline
for _ in range(int(input())):
    ans=0
    n=int(input())
    a=list(map(int,input().split()))
    M=max(a)
    if M!=a[0] and M!=a[-1]:
        print(-1)
        continue
    else:
        if M==a[0]:
            a.pop(0)
        else:
            a.pop()
        mid=len(a)//2
        l=a[:mid]
        r=a[mid:]
        l.reverse()
        r.reverse()
        p=l+[M]+r
        for i in p:
            print(i,end=' ')
    print()