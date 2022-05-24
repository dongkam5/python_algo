# 백준 2225 합분해
import math
N, K = map(int, input().split())
answer = math.comb(N+K-1, K-1)
print(answer % 1000000000)
