n = int(input())
cnt=0
while(True):
    if n%5==0:
        cnt+=int(n/5)
        break
    n=n-3
    cnt+=1
    if n==0:
        break
    elif (n//3)==0:
        cnt=-1
        break
print(cnt)