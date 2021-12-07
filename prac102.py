#백준 3135

A,B=map(int,input().split())
n=int(input())
d=abs(A-B)
go=0
for i in range(n):
    x=int(input())
    if d>abs(x-B):
        d=abs(x-B)
        go=1
print(d+go)