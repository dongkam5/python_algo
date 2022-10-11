# 백준 4375 1
import sys
input = sys.stdin.readline
while True:
    ans = 1
    a = 1
    s = input().rstrip()
    if s:
        num = int(s)
        while True:
            if a % num == 0:
                print(ans)
                break
            else:
                a *= 10
                a += 1
                ans += 1
    else:
        break
