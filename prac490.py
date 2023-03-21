#백준 1992 쿼드트리
import sys
input=sys.stdin.readline
N=int(input())
field=[]
for _ in range(N):
    field.append(list(map(int,input().rstrip())))
answer=''
def compress(R,C,N):
    global answer
    criteria=field[R][C]
    for i in range(R,R+N):
        for j in range(C,C+N):
            if criteria!=field[i][j]: #만약 모든 값이 같지 않으면
                answer+='(' #괄호 시작
                compress(R,C,N//2)  # 재귀로 반복
                compress(R,C+N//2,N//2)
                compress(R+N//2,C,N//2)
                compress(R+N//2,C+N//2,N//2)
                answer+=')' #괄호 마침
                return
    if criteria==1: #모든 값이 1이면
        answer+='1'
    elif criteria==0: #모든 값이 0이면
        answer+='0'
compress(0,0,N)
print(answer)