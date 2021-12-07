#백준 14469

n=int(input())
lst=[]

for i in range(n):
    s=list(map(int,input().split()))
    lst.append(s)
lst.sort()
time=0

for arr in lst:
    time=max(time,arr[0])
    time+=arr[1]

print(time)