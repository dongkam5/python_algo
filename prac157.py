#백준 16206
import sys
n,k=map(int,sys.stdin.readline().split())
lst=list(map(int,sys.stdin.readline().split()))
ans=0
check=0
lst.sort()
for i in range(n):
    if lst[i]%10==0:
        num=lst[i]//10
        k-=(num-1)
        ans+=num
    if k<0:
        check=1
        break
if check==1:
    print(ans-(0-k+1))
else:
    for i in range(n):
        if lst[i]%10!=0 and lst[i]>10:
            num=lst[i]//10
            k-=(num)
            ans+=num
        if k<0:
            check=1
            break
    if check==1:
        print(ans-(0-k))
    else:
        print(ans)