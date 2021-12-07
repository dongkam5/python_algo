#백준 9613
import sys
import math
input=sys.stdin.readline
for _ in range(int(input())):
    S=[]
    lst=list(map(int,input().split()))
    n=lst.pop(0)
    for i in range(n-1):
        for j in range(i+1,n):
            k=math.gcd(lst[i],lst[j])
            S.append(k)
    print(sum(S))