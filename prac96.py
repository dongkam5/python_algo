#백준 11508
n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)

ans=0

for i in range(n):
    if (i+1)%3==0:
        pass
    else:
        ans+=lst[i]

print(ans)