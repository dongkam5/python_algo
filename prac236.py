#백준 3036
import sys
import math
input=sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))
cre=lst.pop(0)
for i in lst:
    d=math.gcd(i,cre)
    i//=d
    c=cre//d
    print('{}/{}'.format(c,i))