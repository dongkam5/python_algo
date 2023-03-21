#백준 7662 이중 우선순위 큐
import heapq
import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    k=int(input())
    minh=[]
    maxh=[]
    temp=[]
    length=0
    for _ in range(k):
        cmd,mode=map(str,input().split())
        mode=int(mode)
        if cmd=='I':
            heapq.heappush(minh,mode)
            heapq.heappush(maxh,-mode)
            length+=1
        elif length>=1:
            length-=1
            if mode==1:
                heapq.heappop(maxh)
            elif mode==-1:
                heapq.heappop(minh)
        if length==0:
            minh.clear()
            maxh.clear()
    while maxh:
        temp.append(-heapq.heappop(maxh))
    minh_set=set(minh)
    maxh_set=set(temp)
    print(minh)
    print(temp)
    common=(minh_set&maxh_set)
    
    if common:
        print(max(common),min(common))
    else:
        print('EMPTY')