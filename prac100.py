#백준 1758

n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)

ans=0

for i in range(n):
    if lst[i]-(i)<=0:
        pass
    else:
        ans+=(lst[i]-i)

print(ans)