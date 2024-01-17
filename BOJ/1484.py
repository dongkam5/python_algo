#백준 1484

G=int(input())

a=1
b=2
ans=[]
while (a+b)<=G:
    a=1
    while a<b:
        if ((b+a)*(b-a))==G:
            ans.append(b)
        a+=1
    b+=1

if ans:
    for a in ans:
        print(a)
else:
    print(-1)