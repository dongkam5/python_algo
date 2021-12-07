#코드포스 A
import sys
input= sys.stdin.readline
n=int(input())
for i in range(n):
    ans=0
    k=list(map(int,input().rstrip()))
    check=0
    for i in range(len(k)):
        if k[i]%2==0:
            check=1
            break
    if check==0:
        ans=-1
        print(ans)
        continue
    if k[-1]%2==0:
        ans=0
    elif k[0]%2==0:
        ans=1
    else:
        ans=2
    print(ans)