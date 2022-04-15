# 백준 5430 AC
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    p = list(map(str, input()))
    n = int(input().rstrip())
    lst = input().rstrip()[1:-1]
    if lst:
        lst = list(map(str, lst.split(',')))
    if p.count('D') > n:
        print('error')
    elif p.count('D') == n:
        print([])
    else:
        i = 0
        front = 0
        back = 0
        check = 0
        while i < len(p)-1:
            if p[i] == 'R':
                j = 1
                while i+j < len(p):
                    if p[i+j] == 'R':
                        j += 1
                    else:
                        break
                i = i+j
                if j % 2 == 1:
                    if check == 0:
                        check = 1
                    else:
                        check = 0
            else:
                j = 1
                while i+j < len(p)-1:
                    if p[i+j] == 'D':
                        j += 1
                    else:
                        break
                i = i+j
                if check == 0:
                    front += j
                else:
                    back += j
        lst = lst[front:len(lst)-back]
        if check == 1:
            lst.reverse()
        print('['+','.join(lst)+']')
