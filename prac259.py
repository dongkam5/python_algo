#백준 1969
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
lst=[[0]*(4) for _ in range(M)]
for i in range(N):
    s=list(map(str,input()))
    for k in range(M):
        if s[k]=='A':
            lst[k][0]+=1
        elif s[k]=='C':
            lst[k][1]+=1
        elif s[k]=='G':
            lst[k][2]+=1
        elif s[k]=='T':
            lst[k][3]+=1
d=0
for i in range(M):
    d+=(N-max(lst[i]))
    if lst[i].index(max(lst[i]))==0:
       print('A',end='')
    elif lst[i].index(max(lst[i]))==1:
        print('C',end='')
    elif lst[i].index(max(lst[i]))==2:
        print('G',end='')
    else:
        print('T',end='')
print()
print(d)