# 프로그래머스 level1 과일 장수
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(m-1,len(score),m):
        answer+=score[i]*m
    return answer
