#코드포스 10/13 div3 C번
import sys
for _ in range(int(sys.stdin.readline())):
    n,k=map(int,sys.stdin.readline().split())
    lst=list(map(int,sys.stdin.readline().split()))
    lst.sort(reverse=True)
    cat=0
    move=0
    ans=0
    for i in range(k):
        if lst[i]>cat:
            move=n-lst[i]
            cat+=move
            ans+=1
    print(ans)