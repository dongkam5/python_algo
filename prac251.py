#백준 11660 pypy3로 풀림
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
lst=[]
for i in range(N):
    s=list(map(int,input().split()))
    for i in range(1,N):
        s[i]+=s[i-1]
    lst.append(s)
for _ in range(M):
    x1,y1,x2,y2=map(int,input().split())
    sum=0
    for i in range(x1-1,x2):
        if y1==1:
            sum+=lst[i][y2-1]
        else:
            sum+=(lst[i][y2-1]-lst[i][y1-2])
    print(sum)