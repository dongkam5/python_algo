#백준 16435
N,L=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
for i in range(N):
    if lst[i]<=L:
        L+=1
    else:
        break

print(L)