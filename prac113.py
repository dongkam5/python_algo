#백준 2872
import sys
n=int(sys.stdin.readline())
M=0
ans=0
for i in range(n):
    k=int(sys.stdin.readline())
    if k>M:
        M=k 
    else:
        ans=max(ans,k)

print(ans)
