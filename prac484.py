#백준 11659 구간 합 구하기
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
l=list(map(int,input().split()))
s={0:0}
for i in range(N):
    s[i+1]=(s[i]+l[i])
for _ in range(M):
    start,end=map(int,input().split())
    ans=s[end]-s[start-1]
    print(ans)

''' 다른 풀이
#백준 11659 구간 합 구하기
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
l=list(map(int,input().split()))
s=[0]
for i in range(N):
    s.append(s[i]+l[i])
for _ in range(M):
    start,end=map(int,input().split())
    ans=s[end]-s[start-1]
    print(ans)
'''