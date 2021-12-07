#백준 2012
n=int(input())
lst=[]
ans=0
for i in range(n):
    lst.append(int(input()))
lst.sort()

for i in range(n):
        ans+=abs(lst[i]-(i+1))
print(ans)