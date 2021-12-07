#코드포스 10/13 div3 D번
import sys
from math import *
for _ in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    lst=list(map(int,sys.stdin.readline().split()))
    d=abs(lst[1]-lst[0])
    for i in range(1,n-1):
        recent=abs(lst[i+1]-lst[i])
        d=gcd(d,recent)
    if d==0:
        print(-1)
    else:
        print(d)