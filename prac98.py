#백준 2847

n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
check=0

for i in range(n-2,-1,-1):
    if lst[i]>=lst[i+1]:
        check+=(lst[i]-lst[i+1]+1)
        lst[i]-=(lst[i]-lst[i+1]+1)

print(check)