#백준 1448
import sys
n=int(sys.stdin.readline())
lst=[]
for i in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort(reverse=True)
check=0
ans=0
for i in range(n-2):
    if lst[i]<(lst[i+1]+lst[i+2]):
        check=1
        ans+=(lst[i]+lst[i+1]+lst[i+2])
        break

if check==0:
    print(-1)
else:
    print(ans)