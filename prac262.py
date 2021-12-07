#프로그래머스 정수삼각형
def solution(triangle):
    leng=len(triangle)
    for i in range(1,leng):
        for j in range(i+1):
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j==i:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j],triangle[i-1][j-1])
    answer = 0
    answer=max(triangle[leng-1])
    return answer