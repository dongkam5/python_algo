#백준 1874
import sys
input = sys.stdin.readline

N = int(input())
arr = [0]*(100001)
answer = []
prev = 0
check = 0
for _ in range(N):
    curr = int(input())
    if arr[curr] == 1:
        check = 1
        break
    else:
        if curr >= prev:
            for i in range(prev+1, curr+1, 1):
                if arr[i] == 0:
                    answer.append('+')
            arr[curr] = 1
            answer.append('-')
            prev = curr-1
        else:
            for i in range(prev, curr-1, -1):
                if arr[i] == 0:
                    answer.append('-')
                    arr[i] = 1
            prev = curr-1
if check == 1:
    print('NO')
else:
    for ele in answer:
        print(ele)
