# 백준 6588 골드바흐의 추측
import sys
input = sys.stdin.readline


def isPrime(num):
    i = 3
    while i**2 <= num:
        if num % i == 0:
            return 0
        i += 1
    return 1


while True:
    check = 0
    n = int(input().rstrip())
    if n == 0:
        break
    for i in range(3, n+1, 2):
        n1 = i
        n2 = n-i
        if n1 > n2:
            break
        else:
            check = isPrime(n1)+isPrime(n2)
            if check == 2:
                break
    if check != 2:
        print("Goldbach's conjecture is wrong.")
    else:
        print("{} = {} + {}".format(n, n1, n2))
