#백준 11497
import sys
from collections import deque
tc=int(sys.stdin.readline())
for _ in range(tc):
    dq=deque([])
    n=int(sys.stdin.readline())
    lst=list(map(int,sys.stdin.readline().split()))
    lst.sort()
    for i in range(n):
        if i%2==0:
            dq.append(lst.pop())
        else:
            dq.appendleft(lst.pop())
    M=0
    for i in range(n-1):
        M=max(M,abs(dq[i]-dq[i+1]))
    M=max(M,abs(dq[0]-dq[-1]))
    print(M)