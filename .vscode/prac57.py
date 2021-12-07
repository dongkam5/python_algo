#10819 --> 틀림

n=int(input())
lst=list(map(int,input().split()))
lst.sort()
a1=lst[:len(lst)//2]
a2=lst[len(lst)//2:]
ans=[]
sum=0
while a1 and a2:
    if a2[0]==a1[0]:
        ans.insert(0,a1.pop(0))
        ans.insert(0,a2.pop(1))

    else:
        ans.insert(0,a2.pop(0))
        ans.insert(0,a1.pop(0))
if a2:
    ans.insert(0,a2.pop(0))

for i in range(n-1):
    sum+=abs(ans[i]-ans[i+1])
print(sum)