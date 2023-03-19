#백준 1654 랜선 자르기
K,N=map(int,input().split())
lans=[]
lans_sum=0
lans_avg=0
temp=0
for _ in range(K):
    lan=int(input())
    lans_sum+=lan
    lans.append(lan)
lans_avg=lans_sum//N
temp=lans_avg
while temp>0:
    cnt=0
    for lan in lans:
        cnt+=lan//temp
    if cnt>=N:
        answer=temp
        break
    temp-=1

print(answer)