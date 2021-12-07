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
    M1_index=s.index(max(s))
    M1=s.pop(M1_index)
    M2_index=s.index(max(s))
    M2=s.pop(M2_index)
    count=0
    if M1>=n/2 and M2>=n/2:
        for k in range(n):
            if data[k][M1_index]==data[k][M2_index]:
                count+=1
        if M1-count==M2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
        break