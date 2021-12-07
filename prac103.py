#백준 20363

X,Y=map(int,input().split())

ans=0

if X>Y:
    ans+=(X+Y+Y//10)
else:
    ans+=(Y+X+X//10)

print(ans)