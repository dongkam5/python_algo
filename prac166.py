#백준 6571
import sys
dp=[0]*(10001)
dp[1]=1
dp[2]=2
for i in range(3,501):
    dp[i]=dp[i-1]+dp[i-2]
while True:
    count=0
    a,b=map(int,sys.stdin.readline().split())
    if a==0 and b==0:
        break
    else:
        for i in range(1,501):
            if a<=dp[i]<=b:
                count+=1
            elif dp[i]>b:
                break
    print(count)