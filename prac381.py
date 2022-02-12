# 백준 10775
import sys
input = sys.stdin.readline
G = int(input())
P = int(input())
park = [0]*(G+1)
check = 0
for i in range(P):
    g = int(input())
    if check == 0:
        if park[g] == 0:
            park[g] = 1
        else:
            j = 1
            while g-j >= 1 and park[g-j] != 0:
                j += 1
            if g-j == 0:
                check = 1
            else:
                park[g-j] = 1
print(park.count(1))
