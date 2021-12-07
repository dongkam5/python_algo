#백준 14241
import sys
import heapq
n=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
heapq.heapify(lst)
ans=0
for i in range(n-1):
    x=heapq.heappop(lst)
    y=heapq.heappop(lst)
    ans+=x*y
    heapq.heappush(lst,x+y)
print(ans)
'''import sys
n=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
ans=0
for i in range(n-1):
    lst.sort()
    x=lst.pop(0)
    y=lst.pop(0)
    lst.append(x+y)
    ans+=(x*y)
print(ans)'''