#백준 1946 못품
import sys
for _ in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    ans=0
    M=0
    lst=[]
    for i in range(n):
        lst.append(list(map(int,sys.stdin.readline().split())))
    lst.sort(key=lambda x:(x[0],x[1]))
    M=lst[0][1]
    for i in range(1,n):
        if M>lst[i][1]:
            M=lst[i][1]
            ans+=1
    print(ans+1)