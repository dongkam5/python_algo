lst=[]
sum=0
count=0
for i in range(9):
    n=int(input())
    sum+=n
    lst.append(n)
for i in range(8):
    for j in range(i+1,9):
        if sum==(100+lst[i]+lst[j]):
            a=lst[i]
            b=lst[j]
lst.remove(a)
lst.remove(b)
lst.sort()
for i in lst:
    print(i)