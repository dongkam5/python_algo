#백준 11501
for i in range(int(input())):
    d=int(input())
    lst=list(map(int,input().split()))
    ans=0
    M=0
    for i in range(d-1,0,-1):
        M=max(M,lst[i])
        if M>lst[i-1]:
            ans+=(M-lst[i-1])
        else:
            pass
    print(ans)