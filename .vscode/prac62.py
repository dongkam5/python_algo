#프로그래머스 level2 스파이위장
def solution(clothes):
    answer = 0
    lst_num=[1]*(31)
    lst=[]
    for clothe in clothes:
        category=clothe[1]
        if category not in lst:
            lst.append(category)
            lst_num[lst.index(category)]+=1
        else:
            lst_num[lst.index(category)]+=1
    
    for i in lst_num:
        answer=answer*i
    answer=answer-1
    return answer

'''다른사람 코드
def solution(clothes):
    answer={}
    for i in clothes:
        if i[1] in answer: answer[i[1]]+=1
        else: answer[i[1]]=1
    cnt=1
    for i in answer.values():
        cnt*=(i+1)
    return cnt-1
'''