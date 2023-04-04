#프로그래머스 level1 푸드파이트 대회
def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer+=(food[i]//2)*str(i)
    answer=answer+"0"+answer[::-1]
    return answer
