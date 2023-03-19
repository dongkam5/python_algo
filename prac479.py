#백준 1654 랜선 자르기
K,N=map(int,input().split())
lans=[]
lans_sum=0
lans_end=0
lans_start=0
temp=0
answer=0
for _ in range(K):
    lan=int(input())
    lans_sum+=lan
    lans.append(lan)
lans_end=(lans_sum//N)+1

while True:
    cnt=0
    if lans_start==lans_end:
        break
    temp=(lans_end+lans_start)//2
    for lan in lans:
        cnt+=lan//temp
        if cnt>=N:
            answer=temp
            lans_start=temp+1
            break
    if cnt<N:
        lans_end=(temp)

print(answer)