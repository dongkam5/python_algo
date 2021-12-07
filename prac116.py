#백준 13417
import sys
from collections import deque
for tc in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    lst=list(map(str,sys.stdin.readline().split()))
    d=deque()
    d.append(lst.pop(0))
    for i in range(n-1):
        if d[0]>=lst[0]:
            d.appendleft(lst.pop(0))
        else:
            d.append(lst.pop(0))
    print(''.join(d))