# 백준 14891 톱니바퀴
from collections import deque
import sys
input = sys.stdin.readline
one = deque(list(map(int, input().rstrip())))
two = deque(list(map(int, input().rstrip())))
three = deque(list(map(int, input().rstrip())))
four = deque(list(map(int, input().rstrip())))
match = {1: one, 2: two, 3: three, 4: four}
K = int(input())


def turn_clock(s):
    s.appendleft(s.pop())


def return_clock(s):
    s.append(s.popleft())


def check(num):
    right = num+1
    left = num-1
    if 1 <= left < 5 and match[num][6] != match[left][2] and visited[left] == 0:
        nums.appendleft(left)
        visited[left] = 1
        check(left)
    if 1 <= right < 5 and match[num][2] != match[right][6] and visited[right] == 0:
        nums.append(right)
        visited[right] = 1
        check(right)


for _ in range(K):
    num, direc = map(int, input().split())
    nums = deque([])
    visited = [0]*(5)
    nums.append(num)
    visited[num] = 1
    check(num)
    ind = nums.index(num)
    if ind % 2 == 1:
        if direc == 1:
            direc = -1
        else:
            direc = 1
    for num in nums:
        if direc == 1:
            turn_clock(match[num])
            direc = -1
        else:
            return_clock(match[num])
            direc = 1

answer = 0
wei = 1
for val in match.values():
    answer += val[0]*wei
    wei *= 2
print(answer)
