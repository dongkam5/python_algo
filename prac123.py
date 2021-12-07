#코드포스 A번 문제
import sys
for i in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    check=0
    row1=list(map(str,sys.stdin.readline()))
    row2=list(map(str,sys.stdin.readline()))
    for i in range(n):
        if row1[i]=='1' and row2[i]=='1':
            check=1
            break
    if check==1:
        print('NO')
    else:
        print('YES')
