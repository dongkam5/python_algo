# 백준 9935 문자열 폭발
s = list(map(str, input().rstrip()))
burst = list(map(str, input().rstrip()))
burst_len = len(burst)
stack = []

for i in range(len(s)):
    val = s[i]
    stack.append(val)
    if len(stack) >= burst_len and val == burst[burst_len-1]:
        for j in range(burst_len-1, -1, -1):
            if stack[len(stack)-burst_len+j] != burst[j]:
                break
        else:
            for _ in range(burst_len):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')
