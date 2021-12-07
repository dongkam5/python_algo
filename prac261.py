#백준 12851
from collections import deque
n,k=map(int,input().split())
visit=[0]*(100001)
queue=deque()
queue.append([n,0])
ans=100000
cnt=0
while queue:
    p,d=queue[0][0],queue[0][1]
    if p==k:
        if ans>queue[0][1]:
            ans=queue[0][1]
            cnt=1
        elif ans==queue[0][1]:
            cnt+=1
    queue.popleft()
    visit[p]=1
    if p-1>=0 and visit[p-1]==0:
        queue.append([p-1,d+1])
    if p+1<=100000 and visit[p+1]==0:
        queue.append([p+1,d+1])
    if p*2<=100000 and visit[p*2]==0:
        queue.append([p*2,d+1])

print(ans)
print(cnt)