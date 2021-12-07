#백준 2217

from math import *
n=int(input())
s=[]

for i in range(n):
    s.append(int(input()))
s.sort(reverse=True)

ans=0

for i in range(n):
    ans=max(ans,s[i]*(i+1))

print(floor(ans))