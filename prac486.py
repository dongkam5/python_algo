#백준 18870 좌표 압축
import sys
input=sys.stdin.readline
N=int(input()) 
l=list(map(int,input().split())) #리스트에 저장
temp=list(map(int,l)) # 좌표 압축을 진행하기 위해 임시 리스트(temp) 생성
temp=list(set(temp)) # temp의 중복 제거
temp.sort() # temp를 정렬
compress={}
answer=[]
for i in range(len(temp)):
    compress[temp[i]]=i #제일 작은 값부터 순서대로 번호를 가지도록 설정

for i in range(N):
    answer.append(compress[l[i]])

print(*answer)