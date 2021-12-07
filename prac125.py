#코드포스 C번 문제
import sys
from math import *
for i in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    lst=list(map(int,sys.stdin.readline().split()))
    SUM=sum(lst)
    k=(float(SUM)/n)
    count=0
    se=set(lst)
    for i in se:
        if (2*k-i) in se:
            if k==i:
                count+=comb(lst.count(i),2)
            else:
                count+=(lst.count(i)*lst.count(2*k-i))/2
    print(int(count))