# 백준 1620 나는야 포켓몬 마스터 이다솜
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
mon_to_digit={}
digit_to_mon={}
for i in range(1,N+1):
    monster=str(input().rstrip())
    mon_to_digit[monster]=i
    digit_to_mon[str(i)]=monster
for _ in range(M):
    val=input().rstrip()
    if mon_to_digit.get(val):
        print(mon_to_digit[val])
    else:
        print(digit_to_mon[val])


''' 더 좋은 풀이
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])
'''