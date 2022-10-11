# 백준 10828 스택
import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    cmd = list(map(str, input().split()))
    len_s = len(stack)
    if len(cmd) == 2:
        stack.append(cmd[1])
    elif cmd[0] == 'top':
        if len_s > 0:
            print(stack[-1])
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len_s)
    elif cmd[0] == 'pop':
        if len_s > 0:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == 'empty':
        if len_s == 0:
            print(1)
        else:
            print(0)
