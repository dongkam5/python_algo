#백준 17219 비밀번호 찾기
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
sites={}
for _ in range(N):
    site,password=map(str,input().split())
    sites[site]=password

for _ in range(M):
    target=input().rstrip()
    print(sites[target])