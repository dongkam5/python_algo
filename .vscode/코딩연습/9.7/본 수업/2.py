# 백준 22942 데이터 체커
import sys
input = sys.stdin.readline
N = int(input())
arr = []
check = 0
for _ in range(N):
    x, r = map(int, input().split())
    arr.append([x, r, x-r, x+r])
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if not (arr[i][2] > arr[j][3] or arr[i][3] < arr[j][2] or ((arr[i][2] < arr[j][2]) and (arr[i][3] > arr[j][3])) or ((arr[i][2] > arr[j][2]) and (arr[i][3] < arr[j][3]))):
            check = 1
            break

if check == 1:
    print('NO')
else:
    print('YES')
