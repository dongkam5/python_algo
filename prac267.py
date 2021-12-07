#백준 15663
import sys
from itertools import permutations
n,m=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
permu=permutations(lst,m)
per=set(permu)
perl=list(per)
perl.sort()
for i in perl:
    for k in i:
        print(k,end=' ')
    print()