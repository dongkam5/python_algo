#백준 5545
import sys
from math import *
n=int(sys.stdin.readline())
A,B=map(float,sys.stdin.readline().split())
C=float(sys.stdin.readline())
lst=[]
for i in range(n):
    lst.append(float(sys.stdin.readline()))
lst.sort(reverse=True)
cal=C
won=A
ans=floor(C/A)
for i in range(n):
    if ans<=floor((cal+lst[i])/(won+B)):
        cal+=lst[i]
        won+=B
        ans=floor(cal/won)
    else:
        break

print(ans)