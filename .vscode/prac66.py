#백준 10809

lst=list(map(str,input()))
ans=[-1]*(26)

for i in lst:
    ans[ord(i)-97]=lst.index(i)

for i in ans:
    print(i,end=' ')