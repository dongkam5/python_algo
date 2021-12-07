#백준 20413
import sys
n=int(sys.stdin.readline())
cri=list(map(int,sys.stdin.readline().split()))
lst=list(map(str,sys.stdin.readline().rstrip()))
money=[0]*(n+1)
for i in range(n):
    if lst[i]=='B':
        money[i+1]=(cri[0]-money[i]-1)
    elif lst[i]=='S':
        money[i+1]=(cri[1]-money[i]-1)
    elif lst[i]=='G':
        money[i+1]=(cri[2]-money[i]-1)
    elif lst[i]=='P':
        money[i+1]=(cri[3]-money[i]-1)
    elif lst[i]=='D':
        money[i+1]=cri[3]

print(sum(money))