#백준 12904

import sys

S=str(input())
T=list(map(str,sys.stdin.readline().rstrip()))

len_S=len(S)
len_T=len(T)

is_front=True
is_first=True
while len_S<len_T:
    if is_front:
        if T[-1]=='A':
            T.pop()
        else:
            if not is_first:
                T.pop()
                is_front=False
            else:
                is_first=False
                is_front=False
    else:
        if T[0]=='A':
            T.pop(0)
        else:
            T.pop(0)
            is_front=True
    len_T-=1

T=''.join(T)
if S==T:
    print(1)
else:
    print(0)