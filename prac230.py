# 백준 1927 최소힙
import sys
import heapq
input=sys.stdin.readline
q=[]
n=int(input())

for _ in range(n):
    k=int(input())
    if k==0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q,k)
