#프로그래머스 n^2배열 자르기
def solution(n, left, right):
    answer = []
    s_row=left//n
    s_col=left%n
    e_row=right//n
    e_col=right%n
    if s_row<e_row:
        for i in range(s_col,n):
            M=max(s_row,i)
            answer.append(M+1)
        for i in range(s_row+1,e_row):
            for j in range(n):
                M=max(i,j)
                answer.append(M+1)
        for i in range(e_col+1):
            M=max(e_row,i)
            answer.append(M+1)
    else:
        for i in range(s_col,e_col+1):
            M=max(s_row,i)
            answer.append(M+1)
    return answer
