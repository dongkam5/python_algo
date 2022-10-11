# 백준 17427 약수의 합 2
n = int(input())
ans = 0
temp = 1
while temp <= n:
    ans += (n//temp)*temp
    temp += 1

print(ans)
