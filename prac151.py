#백준 1263
import sys
n=int(sys.stdin.readline())
lst=[]
for i in range(n):
    s=list(map(int,sys.stdin.readline().split()))
    lst.append(s)
lst.sort(key=lambda x:x[1])
ans=-1
start=lst[0][1]-lst[0][0]
if start<0:
    print(ans)
else:
    for time in range(start,-1,-1):
        count=0
        ini_time=time
        for k in range(len(lst)):
            if time+lst[k][0]<=lst[k][1]:
                time+=lst[k][0]
                count+=1
            else:
                break
        if count==n:
            ans=ini_time
            break
        if ini_time==0:
            break
    print(ans)