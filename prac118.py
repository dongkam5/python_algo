#백준 12018
import sys
n,m=map(int,(sys.stdin.readline().split()))
s=[]
for i in range(n):
    p,l=map(int,sys.stdin.readline().split())
    lst=list(map(int,sys.stdin.readline().split()))
    lst.sort(reverse=True)
    if l>p:
        s.append(1)
    elif l!=1:
        s.append(lst[l-1])
s.sort()
ans=0
while m>=0 and len(s)!=0:
    m-=s.pop(0)
    ans+=1
if m>=0:
    print(ans)
else:
    print(ans-1)