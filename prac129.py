#백준 1541
import sys
s=sys.stdin.readline().rstrip()
lst=list(map(str,s.split('-')))
for i in range(len(lst)):
    if '+' in lst[i]:
        k=list(map(int,lst[i].split('+')))
        lst[i]=sum(k)
    else:
        lst[i]=int(lst[i])
ans=lst[0]
for i in range(1,len(lst)):
    ans-=lst[i]

print(ans)

''' 다른풀이
a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)
'''