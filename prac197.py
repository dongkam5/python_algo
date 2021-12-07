#백준 1388
import sys
N,M=map(int,sys.stdin.readline().split())
lst=[]
for _ in range(N):
    lst.append(list(map(str,sys.stdin.readline())))
ans=0
checked=[[0]*(M) for _ in range (N)]

for i in range(N):
    for j in range(M):
        if checked[i][j]==0:
            if lst[i][j]=='-':
                ans+=1
                k=1
                while j+k<M:
                    if lst[i][j+k]=='-':
                        checked[i][j+k]=1
                        k+=1
                    else:
                        break 
            elif lst[i][j]=='|':
                ans+=1
                k=1
                while i+k<N:
                    if lst[i+k][j]=='|':
                        checked[i+k][j]=1
                        k+=1
                    else:
                        break  

print(ans)