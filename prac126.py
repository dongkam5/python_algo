#코드포스 B번 문제
import sys
for i in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    s=[0]*5
    data=[]
    for k in range(n):
        lst=list(map(int,sys.stdin.readline().split()))
        data.append(lst)
        s[0]+=lst[0]
        s[1]+=lst[1]
        s[2]+=lst[2]
        s[3]+=lst[3]
        s[4]+=lst[4]
    check=0
    for i in range(4):
        for j in range(i+1,5):
            count=0
            if s[i]>=(n/2) and s[j]>=(n/2):
                for k in range(n):
                    if data[k][i]==1 and data[k][j]==1:
                        count+=1
                if s[i]>s[j] and (s[i]-s[j])<=count and (s[i]-s[j])%2==count%2:
                    print('YES')
                    check=1
                    break
                elif s[i]<=s[j] and s[j]-count<=s[i] and (s[j]-s[i])%2==count%2:
                    print('YES')
                    check=1
                    break
        if check==1:
            break
    if check==0:
        print('NO')
