#코드포스 10/13 div3 A번
import sys
for _ in range(int(sys.stdin.readline())):
    a,b,c=map(int,sys.stdin.readline().split())
    M=max(a,b,c)
    if M==a and M!=b and M!=c:
        print(0,M-b+1,M-c+1)
    elif M!=a and M==b and M!=c:
        print(M-a+1,0,M-c+1)
    elif M!=a and M!=b and M==c:
        print(M-a+1,M-b+1,0)
    else:
        print(M-a+1,M-b+1,M-c+1)