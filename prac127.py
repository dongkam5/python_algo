#코드포스 C번 문제
import sys
from math import *
for i in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    lst=list(map(int,sys.stdin.readline().split()))
    SUM=sum(lst)
    k=2*(float(SUM)/n)
    count=0
    lst.sort()
    i=0
    j=len(lst)-1
    while i<j:
        if lst[i]+lst[j]==k and lst[i]==(k/2):
            i_count=lst.count(lst[i])
            count+=comb(i_count,2)
            i+=i_count
        elif lst[i]+lst[j]==k:
            i_count=lst.count(lst[i])
            j_count=lst.count(lst[j])
            j-=j_count
            i+=i_count
            count+=(i_count*j_count)
        elif lst[i]+lst[j]<k:
            i+=1
        elif lst[i]+lst[j]>k:
            j-=1
    print(count)