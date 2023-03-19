#백준 18111 마인크래프트
import sys
input=sys.stdin.readline

N,M,B=map(int,input().split())
field=[]
block_sum=0
block_max=0
ans_cnt,ans_cri=10**9,-10**9
for _ in range(N):
    line=list(map(int,input().split()))
    block_max=max(block_max,max(line))
    block_sum+=sum(line)
    field.append(line)
block_avg=block_sum//(N*M)
for k in range(block_avg,block_max+1):
    block_needs=0
    cnt=0
    diff=0
    for i in range(N):
        for j in range(M):
            if k>field[i][j]:
                diff=k-field[i][j]
                cnt+=diff
                block_needs+=(diff)
            elif k<field[i][j]:
                diff=field[i][j]-k
                cnt+=diff*2
                block_needs-=(diff)
    if block_needs>B:
        break
    if ans_cnt>cnt:
        ans_cnt=cnt
        ans_cri=k
    elif ans_cnt==cnt and ans_cri<k:
        ans_cnt=cnt
        ans_cri=k

print(ans_cnt,ans_cri)