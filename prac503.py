#프로그래머스 level1 명예의 전당 (1)
def solution(k, score):
    answer = []
    lst=[]
    if k<=len(score):
        for i in range(k):
            lst.append(score[i])
            lst.sort(reverse=True)
            answer.append(lst[i])
        
        for i in range(k,len(score)):
            if lst[k-1]<score[i]:
                lst.pop()
                lst.append(score[i])
                lst.sort(reverse=True)
            answer.append(lst[k-1])
    else:
        for i in range(len(score)):
            lst.append(score[i])
            lst.sort(reverse=True)
            answer.append(lst[i])

    return answer

print(solution(10,[10, 100, 20, 150, 1, 100, 200]))