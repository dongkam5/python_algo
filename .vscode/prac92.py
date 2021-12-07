#백준 11256

for i in range(int(input())):
    ans=0
    J,N=map(int,input().split())
    s=[]
    for i in range(N):
        c,r=map(int,input().split())
        s.append(c*r)
    s.sort(reverse=True)
    for i in s:
        if J<=0:
            break
        J=J-i
        ans+=1
    print(ans)
