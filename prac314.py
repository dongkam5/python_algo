#코드포스 B
import sys
input=sys.stdin.readline
n=int(input())
for i in range(n):
    ans=0
    a,b=map(int,input().split())
    while a+b>=4 and a>=1 and b>=1:
        if a>b:
            if a//3>=b:
                ans+=b
                b=0
            else:
                ans+=(a-b)//2
                b=b-(a-b)//2
                a=b
        elif a==b:
            ans+=(a//2)
            a=0
            b=0
        else:
            if b//3>=a:
                ans+=a
                a=0
            else:
                ans+=(b-a)//2
                a=a-((b-a)//2)
                b=a        
    print(ans)