#프로그래머스 완주하지 못한 선수
def solution(participant, completion):
    answer = ''
    lst={}
    for i in range(len(participant)):
        if participant[i] in lst:
            lst[participant[i]]+=1
        else:
            lst[participant[i]]=1
    for i in range(len(completion)):
        lst[completion[i]]-=1
    for name,val in lst.items():
        if val==1:
            answer=name

    return answer

''' 다른사람풀이
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''