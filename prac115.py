#백준 18310
from math import *
import sys
n=int(sys.stdin.readline())
lst=list(map(int,input().split()))
ans=0
lst.sort()
if len(lst)%2==0:
    ans=lst[(len(lst)//2)-1]
else:
    ans=lst[(len(lst)//2)]

print(ans)