E,S,M=map(int,input().split())
ans=max(E,S,M)
while (True):
    if (ans-E)%15==0 and (ans-S)%28==0 and (ans-M)%19==0:
        break
    ans+=1
print(ans)