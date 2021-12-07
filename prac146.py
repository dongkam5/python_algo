#백준 11509 못푼 문제 풀이
import sys
n=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
ans=0
arrow=[0]*(1000001)

for i in range(len(lst)):
    if arrow[lst[i]]==0:
        ans+=1
        arrow[lst[i]-1]+=1
    else:
        arrow[lst[i]]-=1
        arrow[lst[i]-1]+=1

print(ans)
