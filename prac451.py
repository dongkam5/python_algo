# 백준 1011 Fly me to the Alpha Centauri
import sys
import math
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    dist = b-a
    val = int(math.sqrt(dist))
    dist = dist-val**2
    answer = val*2-1
    if dist % val == 0:
        answer += dist//val
    else:
        answer += dist//val+1
    print(answer)
