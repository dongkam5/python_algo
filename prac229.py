#백준 11279 최대힙
import sys
import heapq
input=sys.stdin.readline
q=[]
n=int(input())

for _ in range(n):
    k=int(input())
    if k==0:
        if q:
            print((-1)*heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q,-k)
