n,k=map(int,input().split())
index=0
lst=[]
ans=[]
for i in range(n):
    lst.append(i+1)

i=0
while(len(lst)>1):
    i=(i+k-1)%len(lst)
    ans.append(lst.pop((i)%len(lst)))

ans.append(lst[0])
print('<',end='')
for i in range(n-1):
    print(ans[i],end=', ')
print(ans[-1],end='')
print('>')
