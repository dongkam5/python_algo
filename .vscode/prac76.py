#백준 1309

n=int(input())

dp=[0]*(100001)
dp[0]=2
dp[1]=3
dp[2]=7
sum=5
for i in range(3,100001):
    dp[i]=(dp[i-1]+2*(sum))%9901
    sum+=dp[i-1]


print(dp[n])

''' 
다른풀이

n = int(input())
s = [[0] * 3 for i in range(100001)]
for i in range(3):
    s[1][i] = 1
for i in range(2, 100001):
    s[i][0] = s[i - 1][1] + s[i - 1][2] % 9901
    s[i][1] = s[i - 1][0] + s[i - 1][2] % 9901
    s[i][2] = s[i - 1][0] + s[i - 1][1] + s[i - 1][2] % 9901
print(sum(s[n]) % 9901)

'''