#백준 20310
import sys
s=list(map(str,sys.stdin.readline().rstrip()))
zero_count=s.count('0')
one_count=s.count('1')
leng=len(s)
check=0
i=0
while i<leng:
    if check<(one_count//2):
        if s[i]=='1':
            s.pop(i)
            check+=1
            i-=1
        i+=1
    else:
        break
check=0
for i in range(leng-(one_count//2)-1,-1,-1):
    if check<(zero_count/2):
        if s[i]=='0':
            s.pop(i)
            check+=1
    else:
        break
print(''.join(s))