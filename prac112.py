#백준 12845
n=int(input())
lst=list(map(int,input().split()))

lst.sort()
ans=0
for i in range(n-1):
    ans+=lst[i]+lst[-1]

print(ans)