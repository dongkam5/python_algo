# 백준 11758 CCW
import math

P1 = list(map(int, input().split()))
P2 = list(map(int, input().split()))
P3 = list(map(int, input().split()))

if P2[0] != P1[0]:
    a = (P2[1]-P1[1])/(P2[0]-P1[0])
    b = -a*P1[0]+P1[1]
    if P1[0] > P2[0]:
        if round(a*P3[0]+b) == P3[1]:
            print(0)
        elif a*P3[0]+b > P3[1]:
            print(1)
        else:
            print(-1)
    else:
        if round(a*P3[0]+b) == P3[1]:
            print(0)
        elif a*P3[0]+b > P3[1]:
            print(-1)
        else:
            print(1)

else:
    if P1[1] < P2[1]:
        if P1[0] == P3[0]:
            print(0)
        elif P3[0] > P1[0]:
            print(-1)
        else:
            print(1)
    else:
        if P1[0] == P3[0]:
            print(0)
        elif P3[0] > P1[0]:
            print(1)
        else:
            print(-1)
