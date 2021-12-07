#백준 17087
def gcd(a,b):
    while b:
        mod=b
        b=a%b
        a=mod
    return a

n,s=map(int,input().split())
lst=list(map(int,input().split()))
d=[]
for i in lst:
    d.append((abs(s-i)))
m=min(d)
for i in range(len(d)):
    m=gcd(d[i],m)

print(m)