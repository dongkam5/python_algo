#백준 9657
n=int(input())
dp=[0,1,0,1,1]
for i in range(5,n+1):
    if (dp[i-4]+1)==1 or (dp[i-3]+1)==1 or (dp[i-1]+1)==1:
        dp.append(1)
    else:
        dp.append(0)
if dp[n]==1:
    print('SK')
else:
    print('CY')