#백준 2865
n,m,k=map(int,input().split())

s=[0]*(n+1)

for i in range(m):
    arr=list(map(float,input().split()))
    while len(arr)!=0:
        a=int(arr.pop(0))
        s[a]=max(s[a],arr.pop(0))

s.sort()
print(round(sum(s[(n-k)+1:]),1))

