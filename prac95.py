#백준 13305

n=int(input())
d=list(map(int,input().split()))
c=list(map(int,input().split()))

ans=0
i=0
min_cost=1000000000

for i in range(len(c)-1):
    if c[i]>min_cost:
        ans+=(min_cost*d[i])
    else:
        ans+=(c[i]*d[i])
        min_cost=c[i]
    
print(ans)