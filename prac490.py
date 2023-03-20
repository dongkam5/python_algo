#백준 1780 종이의 개수
import sys
input=sys.stdin.readline
minusone=0
zero=0
one=0
def all_same(p):
    global minusone #-1로 이루어진 종이의 개수를 담을 전역변수 생성
    global zero #0으로 이루어진 종이의 개수를 담을 전역변수 생성
    global one #1로 이루어진 종이의 개수를 담을 전역변수 생성
    len_p=len(p)    
    zero_cnt=0 #p에서 0의 개수를 담을 로컬변수 생성
    one_cnt=0 #p에서 1의개수를 담을 로컬변수 생성
    minusone_cnt=0 #p에서 -1의 개수를 담을 로컬변수 생성
    for i in range(len_p): #반복문을 돌며 각 개수 카운트
        for j in range(len_p):
            if p[i][j]==0:
                zero_cnt+=1
            elif p[i][j]==1:
                one_cnt+=1
            elif p[i][j]==(-1):
                minusone_cnt+=1
    if zero_cnt==(len_p*len_p): #모두 0으로 이루어져 있으면
        zero+=1
    elif one_cnt==(len_p*len_p): #모두 1로 이루어져 있으면
        one+=1
    elif minusone_cnt==(len_p*len_p): #모두 -1로 이루어져 있으면
        minusone+=1
    else: #그렇지 않으면
        rows=[val for val in range(0,len_p+1,len_p//3)] #행을 3분할
        columns=[val for val in range(0,len_p+1,len_p//3)] #열도 3분할
        for i in range(1,len(rows)):
            cut_rows=p[rows[i-1]:rows[i]]
            for j in range(1,len(columns)):
                p_=list(zip(*cut_rows))[columns[j-1]:columns[j]]
                all_same(p_) #재귀로 반복


N=int(input())
paper=[]
for _ in range(N):
    paper.append(list(map(int,input().split())))
ans=all_same(paper)
print(minusone)
print(zero)
print(one)


