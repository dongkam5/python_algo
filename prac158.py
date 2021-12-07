#백준 16953
import sys
A,B=map(int,sys.stdin.readline().split())

count=0
while B>A:
    if B%10==1:
        B=B//10
        count+=1
    elif B%2==0:
        B=B/2
        count+=1
    else:
        break
if A!=B:
    print(-1)
else:
    print(count+1)