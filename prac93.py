#백준 16471

n=int(input())
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
s1.sort()
s2.sort(reverse=True)
i=n-1
j=0
check=0
while i>=0:
    if s1[i]<s2[j]:
        j+=1
        check+=1
    i-=1


if check>=((n+1)/2):
    print('YES')
else:
    print('NO')