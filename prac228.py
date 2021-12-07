#백준 10844
import copy
n=int(input())
dp=[1]*(10)
dp[0]=0
for k in range(1,n):
    lst=copy.deepcopy(dp)
    for i in range(10):
        if i==0:
            dp[0]=lst[1]
        elif i==9:
            dp[9]=lst[8]+lst[9]
        else:
            dp[i]=(lst[i-1]+lst[i+1]+lst[i])
print(sum(dp))
print(dp)