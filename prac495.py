#백준 7662 이중 우선순위 큐
import heapq
import sys
input=sys.stdin.readline
N=int(input())
for _ in range(N):
    T=int(input())
    minh=[]
    maxh=[]
    temp=[]
    for _ in range(T):
        cmd,mode=map(str,input().split())
        mode=int(mode)
        if cmd=='I':
            heapq.heappush(minh,mode)
            heapq.heappush(maxh,-mode)
        elif mode==1:
            heapq.heappop(maxh)
        elif mode==0:
            heapq.heappop(minh)
    while maxh:
        temp.append(-1*heapq.heappop(maxh))
    minh_set=set(minh)
    maxh_set=set(temp)
    common=(minh_set&maxh_set)
    if common:
        print(*common)
    else:
        print('EMPTY')