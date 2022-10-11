# 백준 1935 후위표기식2
import sys
import math
input = sys.stdin.readline
N = int(input())
lst = list(map(str, input().rstrip()))
val = [0]*(26)
for i in range(N):
    val[ord('A')+i-65] = int(input())
i = 0
stack = []
for value in lst:
    if 'A' <= value <= 'Z':
        stack.append(val[ord(value)-65])
    else:
        two = stack.pop()
        one = stack.pop()
        if value == '+':
            stack.append(one+two)
        elif value == '-':
            stack.append(one-two)
        elif value == '*':
            stack.append(one*two)
        elif value == '/':
            stack.append(one/two)
print("{:.2f}".format(stack[0]))
