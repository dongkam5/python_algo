# 백준 1107 리모컨

from itertools import product
num = input()
want = list(map(int, num))
l = len(want)
num = int(num)
n = int(input())
if n == 0:
    use = [i for i in range(10)]
else:
    delbtn = list(map(int, input().split()))
    use = list((set([i for i in range(10)]))-set(delbtn))
    use.sort()
if use:
    if not (len(use) == 1 and use[0] == 0):
        if use[0] == 0:
            big = int(str(use[1])+str(use[0])*l)
        else:
            big = int(str(use[0])*(l+1))
        if l != 1:
            small = int(str(use[-1])*(l-1))
        else:
            small = -1000000
        answer = min(abs(num-100), l-1+(num-small), l+1+(big-num))
    else:
        answer = min(abs(num-100), 1+num)
else:
    answer = abs(num-100)

use = list(map(str, use))
data = product(use, repeat=l)
for p in data:
    val = int(''.join(p))
    answer = min(answer, abs(val-num)+l)

print(answer)
