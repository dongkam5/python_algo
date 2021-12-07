#백준 9237

n=int(input())
lst=list(map(int,input().split()))
lst.sort(reverse=True)
day=0
for i in range(len(lst)):
    day=max(day,lst[i]+(i+1))

print(day+1)