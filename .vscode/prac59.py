import sys, itertools

# 입력
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
# 순열
permu = itertools.permutations(data, n)

lpermu=list(permu)
# 차이가 최대인 값을 넣을 변수
ans=[]
ind=0
for p in lpermu:
    if list(p)==data:
        ind=lpermu.index(p)
        break
ans=list(lpermu(p))
print(''.join(ans))