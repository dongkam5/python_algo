#백준 4097
import sys
while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    else:
        lst=[]
        for i in range(n):
            lst.append(int(sys.stdin.readline()))
        dp=[-10001]*(n)
        for i in range(n):
            dp[i]=max(dp[i],lst[i],dp[i-1]+lst[i])
        print(max(dp))