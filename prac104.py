#백준 20937
n=int(input())
lst=[0]*(500001)
s=map(int,input().split())

for i in s:
    lst[i]+=1
print(max(lst))