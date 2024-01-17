#백준 12904

import sys

sys.setrecursionlimit(1000000)

def check(S,T,is_reverse,len_S,len_T):
    ans=0
    if len_S==len_T:
        if is_reverse==True:
            S.reverse()
        S=''.join(S)
        T=''.join(T)
        if S==T:
            return 1
        else:
            return 0
    else:
        if is_reverse:
            ans+=check(['A']+S,T,is_reverse,len_S+1,len_T)
            ans+=check(S+['B'],T,not is_reverse,len_S+1,len_T)
        else:
            ans+=check(S+['A'],T,is_reverse,len_S+1,len_T)
            ans+=check(['B']+S,T,not is_reverse,len_S+1,len_T)
    return ans

S=list(map(str,sys.stdin.readline().rstrip()))
T=list(map(str,sys.stdin.readline().rstrip()))

len_S=len(S)
len_T=len(T)
is_reverse=False
val=check(S,T,is_reverse,len_S,len_T)

print(val)