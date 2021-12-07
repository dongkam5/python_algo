#백준 11722
n=int(input())
lst=list(map(int,input().split()))
lst.reverse()
dp=[1]*(n+1)
for i in range(n):
    for j in range(i):
        if lst[j]<lst[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))

'''다른풀이

n = int(input())
a = list(map(int, input().split()))
dp = [1 for i in range(n)]
for i in range(1, n):
    s = []
    for j in range(i):
        if a[i] < a[j]:
            s.append(dp[j])
    if not s:
        continue
    else:
        dp[i] += max(s)
print(max(dp))
'''