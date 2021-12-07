#백준 10808

lst=list(map(str,input()))
ans=[0]*(26)

for i in lst:
    ans[ord(i)-97]+=1

for i in ans:
    print(i,end=' ')