#백준 15903
import sys
n,m=map(int,sys.stdin.readline().split())
lst=list(map(int,sys.stdin.readline().split()))
lst.sort()

for i in range(m):
    temp=lst[0]+lst[1]
    lst[0]=temp
    lst[1]=temp
    lst.sort()

print(sum(lst))