#백준 2630 색종이 만들기
import sys
input=sys.stdin.readline
white=0
blue=0
def all_same(p):
    global blue #파란색 종이의 개수를 담을 전역변수 생성
    global white #하얀색 종이의 개수를 담을 전역변수 생성
    len_p=len(p)
    s=0
    for i in range(len_p):
        s+=sum(p[i]) #각 요소의 합을 구함
    if s==(len_p*len_p): #모두 파란색이면
        blue+=1
        return 
    elif s==0: #모두 하얀색이면
        white+=1
        return 
    else: #그렇지 않으면
        rows=[val for val in range(0,len_p+1,len_p//2)] #행을 2분할
        columns=[val for val in range(0,len_p+1,len_p//2)] #열도 2분할
        for i in range(1,len(rows)):
            cut_rows=p[rows[i-1]:rows[i]] #행 자름
            for j in range(1,len(columns)):
                p_=list(zip(*cut_rows))[columns[j-1]:columns[j]] #열도 자름
                all_same(p_) #재귀로 반복


N=int(input())
paper=[]
for _ in range(N):
    paper.append(list(map(int,input().split())))
ans=all_same(paper)
print(white)
print(blue)

