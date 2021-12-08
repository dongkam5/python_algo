#프로그래머스 가장 큰 정사각형 찾기 다른사람풀이

def solution(board):
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j]==1:
                board[i][j]=min(board[i-1][j-1],board[i][j-1],board[i-1][j])+1
    answer = 0
    for i in range(len(board)):
        M=max(board[i])
        answer=max(answer,M)
    return answer**2
