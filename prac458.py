# 백준 1038 감소하는 수
import math
N = int(input())
cnt = 0
i = 0
# 2**10 -1 -1 = 1022
if N > 1022:
    print(-1)
elif N == 0:
    print(0)
else:
    i = 1
    while N < math.comb(10, i):
        N -= math.comb(10, i)
        i += 1
    i = 10**(i-1)
    while N != 0:
        s = list(map(int, str(i)))
        m = 10
        for val in s:
            if val >= m:
                break
            else:
                m = val
        else:
            N -= 1
        i += 1
    print(i-1)
