#코드포스 10/13 div3 B번
import sys
for _ in range(int(sys.stdin.readline())):
    ans=100
    n=list(map(str,sys.stdin.readline()))
    for i in range(len(n)-1,-1,-1):
        if n[i]=='0':
            for j in range(i-1,-1,-1):
                if n[j]=='0' or n[j]=='5':
                    ans=min(ans,len(n)-(i+1)+(i-j-2))
        elif n[i]=='5':
            for j in range(i-1,-1,-1):
                if n[j]=='2' or n[j]=='7':
                    ans=min(ans,len(n)-(i+1)+(i-j-2))
    print(ans)