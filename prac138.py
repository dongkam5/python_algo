#백준 14400
import sys
n=int(sys.stdin.readline())
lst=[]
for _ in range(n):
    s=list(map(int,sys.stdin.readline().split()))
    lst.append(s)
lst.sort(key=lambda x:x[0])
x=lst[len(lst)//2][0]
lst.sort(key=lambda x:x[1])
y=lst[len(lst)//2][1]
ans=0
for i in range(n):
    ans+=(abs(x-lst[i][0])+abs(y-lst[i][1]))

print(ans)