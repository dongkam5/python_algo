#백준 1788
import sys
n=int(input())
k=abs(n)
dp=[0,1]
for i in range(2,k+1):
    dp.append((dp[i-1]+dp[i-2])%1000000000)
if n>0 or (n<0 and n%2==1):
    print(1)
elif n<0 and n%2==0:
    print(-1)
else:
    print(0)
print(dp[k])