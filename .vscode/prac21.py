n,m=map(int,input().split())

five=0
fiv=0
for i in range(m+1,n+1):
    while(True):
        if i%5==0:
            five+=1
            i=i//5
        else:
            break

for i in range(1,n-m+1):
    while(True):
        if i%5==0:
            fiv+=1
            i=i//5
        else:
            break

print(five-fiv)