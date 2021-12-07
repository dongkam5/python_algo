n=int(input())
if n==1:
    print(1)
else:
    count=1
    ans=0
    while(n>=count):
        ans+=(n-(count-1))
        count*=10
    print(ans)
