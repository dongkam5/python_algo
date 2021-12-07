#프로그래머스 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    result=[]
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]!=0:
                result.append(board[i][move-1])
                board[i][move-1]=0
                break
        if len(result)>1:
            if result[-1]==result[-2]:
                answer+=2
                result.pop()
                result.pop() 
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
