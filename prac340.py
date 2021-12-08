#프로그래머스 가장 큰 정사각형 찾기
def solution(board):
    line=0
    N=len(board)
    M=len(board[0])
    for i in range(N):
        l=[1]*(M)
        for j in range(i,N):
            count=0
            cnt=0
            for k in range(M):
                l[k]=board[j][k]*l[k]
                if l[k]==1:
                    count+=1
                elif l[k]==0:
                    cnt=max(cnt,count)
                    count=0
            cnt=max(cnt,count)
            if (j-i+1)<=cnt:
                line=max(line,(j-i+1))
    answer=line**2
    return answer
