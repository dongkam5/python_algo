#백준 2853
import sys
n=int(sys.stdin.readline())
lst=[]
for i in range(n):
    lst.append(int(sys.stdin.readline()))
checked=[0]*(n)
ans=0
for i in range(1,n):
    if checked[i]==0:
        d=lst[i]-lst[0]
        ans+=1
        for j in range(i+1,n):
            if (lst[j]-lst[i])==d:
                checked[j]=1
                lst[i]+=d
print(ans)