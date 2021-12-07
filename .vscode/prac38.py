for tc in range(int(input())):
    M,N,x,y=map(int,input().split())
    T=0
    while (T<M*N):
        if((T-x)%M==0 and (T-y)%N==0):
            break
        T+=1
    if T==M*N:
        print(-1)
    else:
        print(T)