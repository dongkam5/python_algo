#백준 1449

N,L=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
s=[]
for i in range(len(lst)-1):
    s.append(lst[i+1]-lst[i])

ans=0
d=0
i=0
while i<(N-1):
    if d+s[i]>(L-1):
        ans+=1
        i+=1
        d=0
    else:
        d+=s[i]
        i+=1

print(ans+1)
            