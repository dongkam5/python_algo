# 백준 17425 약수의 합
import sys
input = sys.stdin.readline


def divnum(num):
    temp = 0
    sqrtnum = int(num**(0.5))
    for i in range(1, sqrtnum+1):
        if num % i == 0:
            val = num//i
            if val != sqrtnum:
                temp += val
    return temp


val = [0]*(1000001)
for i in range(1, 1000001):
    val[i] = val[i-1]+divnum(i)
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    print(val[n])
