#백준 16162

N,A,D=map(int,input().split())
lst=list(map(int,input().split()))
ans=0
for i in range(N):
    if lst[i]==A:
        ans+=1
        A+=D

print(ans)