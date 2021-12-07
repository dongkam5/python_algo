n=int(input())

lst=list(map(int,input().split()))

ans=[0 for _ in range(n)]

for i in range(n):
   k=lst[i]
   count=0
   for j in range(n):
        if count==k and ans[j]==0:
            ans[j]=(i+1)
            break
        if ans[j]==0:
            count+=1

for b in ans:
    print(b,end=' ')

