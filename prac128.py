#백준 1931
import sys
n=int(sys.stdin.readline())
lst=[]

for i in range(n):
    s=list(map(int,sys.stdin.readline().split()))
    lst.append(s)
lst.sort(key=lambda x:(x[1],x[0]))
ans=0
t=-1
for i in range(n):
    if  lst[i][0]>=t:
        ans+=1
        t=lst[i][1]
print(ans)