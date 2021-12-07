#백준 16500
import sys
s=sys.stdin.readline().rstrip()
n=int(sys.stdin.readline())
lst=[]
dp=['']*(101)
for _ in range(n):
    lst.append(str(sys.stdin.readline().rstrip()))

k=0
for i in lst:
    if i==s[:len(i)]:
        dp[len(i)]=i
while k<len(s):
    for i in lst:
        leng=len(i)
        if i==s[k:k+leng] and dp[k]!='':
            dp[k+leng]=(dp[k]+i)
    k+=1
if dp[len(s)]==s:
    print(1)
else:
    print(0)