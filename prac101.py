#백준 20044

n=int(input())
lst=list(map(int,input().split()))
leng=len(lst)
lst.sort()
m=10000000
for i in range(n):
    m=min(m,lst[i]+lst[leng-1-i])

print(m)