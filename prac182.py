#백준 14430
import sys
N,M=map(int,sys.stdin.readline().split())
lst=[]
for i in range(N):
    s=list(map(int,sys.stdin.readline().split()))
    lst.append(s)
for i in range(1,N):
    lst[i][0]+=lst[i-1][0]
for i in range(1,M):
    lst[0][i]+=lst[0][i-1]
for i in range(1,N):
    for j in range(1,M):
        lst[i][j]+=max(lst[i][j-1],lst[i-1][j])

print(max(max(lst)))