#백준 1106
from sys import stdin,maxsize

C,N=map(int,input().split())

ad=[list(map(int,stdin.readline().split()))for _ in range(N)]

dp=[0]+[maxsize]*(C+100)

for cost,customer in ad:
    for cur_customer in range(customer,C+101):
        dp[cur_customer]=min(dp[cur_customer],dp[cur_customer-customer]+cost)

print(min(dp[C:C+101]))