#백준 9375
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    clothes={}
    n=int(input())
    for i in range(n):
        N,V=input().split()
        if V in clothes:
            clothes[V]+=1
        else:
            clothes[V]=1
    sum=1
    for i in clothes.values():
        sum*=(i+1)
    print(sum-1)

'''다른풀이
from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    s = []
    for j in range(n):
        a, b = input().split()
        s.append(b)
    num = 1
    result = Counter(s)
    for key in result:
        num *= result[key] + 1
    print(num - 1)
'''