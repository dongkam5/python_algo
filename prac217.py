#백준 1083
import sys
n=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
s=int(sys.stdin.readline())
i=0
while s>0:
    i=i%(len(lst)-1)
    if lst[i]<lst[i+1]:
        s-=1
        temp=lst[i]
        lst[i]=lst[i+1]
        lst[i+1]=temp
    i+=1

print(lst)