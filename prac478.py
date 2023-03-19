#백준 1654 랜선 자르기
K,N=map(int,input().split())
lans=[]
lans_sum=0 # 랜선의 총합 
lans_end=0 # 탐색 끝 범위
lans_start=0 #탐색 시작 점위
temp=0 # 탐색 기준점 (중점)
answer=0 # 정답
for _ in range(K): #우선 리스트에 저장
    lan=int(input())
    lans_sum+=lan
    lans.append(lan)
lans_end=(lans_sum//N)+1 #끝점을 초기화

while True:
    cnt=0
    if lans_start==lans_end:
        break
    temp=(lans_end+lans_start)//2 #중점을 설정
    for lan in lans:
        cnt+=lan//temp
        if cnt>=N: # 개수가 N게 이상이면, 정답을 temp로 설정
            answer=temp
            lans_start=temp+1 # lans_start(temp+1)~lans_end의 범위를 탐색
            break
    if cnt<N: # 개수가 N개 이하이면
        lans_end=(temp) # # lans_start~lans_end(temp)의 범위를 탐색

print(answer)