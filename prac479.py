#백준 18111 마인크래프트
import sys
input=sys.stdin.readline

N,M,B=map(int,input().split())
field=[]
block_sum=0 #블럭 높이의 합
block_max=0 # 블럭의 최대 높이
ans_cnt,ans_cri=10**9,-10**9 #정답 시간, 정답 높이
for _ in range(N):
    line=list(map(int,input().split()))
    block_max=max(block_max,max(line))
    block_sum+=sum(line)
    field.append(line)
block_avg=block_sum//(N*M) #블럭의 평균 높이
for k in range(block_avg,block_max+1):
    block_needs=0 #필요한 블럭의 개수
    cnt=0
    diff=0
    for i in range(N):
        for j in range(M):
            if k>field[i][j]:
                diff=k-field[i][j] #가준 높이와 블럭의 높이 차
                cnt+=diff # 걸리는 시간
                block_needs+=(diff) # 필요한 블럭 수
            elif k<field[i][j]:
                diff=field[i][j]-k #가준 높이와 블럭의 높이 차
                cnt+=diff*2 # 걸리는 시간
                block_needs-=(diff) # 필요한 블럭 수
    if block_needs>B: #필요 블럭 개수가 소유한 블럭 개수보다 많으면
        break #못쌓으므로 탈출
    if ans_cnt>cnt: #시간이 더 적게 걸리면 정답 갱신
        ans_cnt=cnt
        ans_cri=k
    elif ans_cnt==cnt and ans_cri<k: #시간이 같을 때, 높이가 더 높으면 정답 갱신
        ans_cnt=cnt
        ans_cri=k

print(ans_cnt,ans_cri)