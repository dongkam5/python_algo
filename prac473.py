# 백준 3085 사탕 게임
import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(str, input().rstrip())))

cnt = 0

for i in range(N):
    for j in range(N):
        temp = lst[i][j]
        if i+1 < N and (lst[i][j] != lst[i+1][j]):
            temp_cnt = 0
            lst[i][j] = lst[i+1][j]
            lst[i+1][j] = temp
            d = 1
            while j+d < N:
                if lst[i][j] == lst[i][j+d]:
                    d += 1
                else:
                    break
            temp_cnt += d
            d = 1
            while j-d >= 0:
                if lst[i][j] == lst[i][j-d]:
                    d += 1
                else:
                    break
            temp_cnt += (d-1)
            cnt = max(cnt, temp_cnt)

            temp_cnt = 0
            d = 1
            while j+d < N:
                if lst[i+1][j] == lst[i+1][j+d]:
                    d += 1
                else:
                    break
            temp_cnt += d
            d = 1
            while j-d >= 0:
                if lst[i+1][j] == lst[i+1][j-d]:
                    d += 1
                else:
                    break
            cnt = max(temp_cnt, cnt)
            lst[i+1][j] = lst[i][j]
            lst[i][j] = temp

        if j+1 < N and lst[i][j] != lst[i][j+1]:
            temp_cnt = 0
            lst[i][j] = lst[i][j+1]
            lst[i][j+1] = temp
            d = 1
            while i+d < N:
                if lst[i][j] == lst[i+d][j]:
                    d += 1
                else:
                    break
            temp_cnt += d
            d = 1
            while i-d >= 0:
                if lst[i][j] == lst[i-d][j]:
                    d += 1
                else:
                    break
            temp_cnt += (d-1)
            cnt = max(cnt, temp_cnt)

            temp_cnt = 0
            d = 1
            while i+d < N:
                if lst[i][j+1] == lst[i+d][j+1]:
                    d += 1
                else:
                    break
            temp_cnt += d
            d = 1
            while i-d >= 0:
                if lst[i][j+1] == lst[i-d][j+1]:
                    d += 1
                else:
                    break
            cnt = max(temp_cnt, cnt)
            lst[i][j+1] = lst[i][j]
            lst[i][j] = temp
print(cnt)
