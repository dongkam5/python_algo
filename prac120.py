#백준 17451
import sys
n=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))

for i in range(n-1,0,-1):
    if lst[i]>lst[i-1]:
        k=lst[i-1]
        j=lst[i]//k
        if lst[i]%lst[i-1]!=0:
            lst[i-1]=k*(j+1)
        else:
            lst[i-1]=k*j
print(lst[0])