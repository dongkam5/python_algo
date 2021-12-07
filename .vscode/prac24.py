n=int(input())
lst=[1,2,4]

for i in range(3,10):
    lst.append(lst[i-1]+lst[i-2]+lst[i-3])

for i in range(n):
    k=int(input())
    print(lst[k-1])