#백준 21314
import sys
from math import *
lst=list(map(str,sys.stdin.readline().rstrip()))
count=0
ans1=[]
ans2=[]
for i in range(len(lst)):
    if lst[i]=='K':
        ans1.append('5')
        ans1.append('0'*count)
        if count!=0:
            ans2.append('1')
            ans2.append('0'*(count-1))
        ans2.append('5')
        count=0
    else:
        count+=1
if count!=0:
    ans1.append('1'*count)
    ans2.append('1')
    ans2.append('0'*(count-1))

print(''.join(ans1))
print(''.join(ans2))
