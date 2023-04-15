#백준 10830 행렬 제곱
import sys
input=sys.stdin.readline
N,B=map(int,input().split())
# 1,000으로 나눈 나머지
matrix=[]
for _ in range(N):
    matrix.append(list(map(int,input().split())))
