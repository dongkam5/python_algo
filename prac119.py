#백준 20115
import sys
n=int(sys.stdin.readline())
lst=list(map(float,sys.stdin.readline().split()))
lst.sort(reverse=True)
ans=lst.pop(0)
for i in range(n-1):
    ans+=lst[i]/2
print(ans)