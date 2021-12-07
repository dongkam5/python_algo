#백준 20365
import sys
n=int(sys.stdin.readline())
lst=list(map(str,sys.stdin.readline().rstrip()))
lst.append('L')
B_count=0
R_count=0
i=0
while i<(len(lst)-1):
    if lst[i]=='B':
        while lst[i]==lst[i+1]:
            i+=1
        B_count+=1
        i+=1
    else:
        while lst[i]==lst[i+1]:
            i+=1
        R_count+=1
        i+=1

print(min(B_count,R_count)+1)
