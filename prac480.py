# 백준 11723 집합
import sys
input=sys.stdin.readline
M=int(input())
S=[]
for _ in range(M):
    cmd=list(map(str,input().split())) 
    if len(cmd)==2:
        command,num=cmd[0],cmd[1] #명령 + 숫자 인 경우
        num=int(num)
    else:
        command=cmd[0] #명령만 있는 경우
    if command=='add': 
        if not S.count(num):
            S.append(num)
    elif command=='remove':
        if S.count(num):
            S.remove(num)
    elif command=='check':
        if S.count(num):
            print(1)
        else:
            print(0)
    elif command=='toggle':
        if S.count(num):
            S.remove(num)
        else:
            S.append(num)
    elif command=='all':
        S=[i for i in range(1,21)]
    elif command=='empty':
        S=[]

