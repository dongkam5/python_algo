#백준 11047
n,k=map(int,input().split())
lst=[]
for i in range (n):
    lst.append(int(input()))
lst.reverse()
coin=0

while k!=0:
    for i in lst:
        if i<=k:
            coin=coin+(k//i)
            k=(k%i)
            lst=lst[lst.index(i):]
            break
print(coin)

