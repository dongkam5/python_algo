# 백준 14719 빗물
H, W = map(int, input().split())
lst = list(map(int, input().split()))
temp = [0]*(H+1)
i = 0
ans = 0
M = lst[0]
while i < W:
    j = 1
    while i+j < W:
        if lst[i+j] <= lst[i+j-1]:
            for k in range(lst[i+j], M):
                temp[k] += 1
        else:
            if lst[i+j] >= M:
                for k in range(0, M):
                    ans += temp[k]
                    temp[k] = 0
                M = lst[i+j]
                break
            else:
                for k in range(0, lst[i+j]):
                    ans += temp[k]
                    temp[k] = 0
                for k in range(lst[i+j], M):
                    temp[k] += 1
        j += 1
    i += j
print(ans)
