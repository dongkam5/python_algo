# 프로그래머스 level1 가장 가까운 글자
from collections import defaultdict
def solution(s):
    answer=[]
    dict_=defaultdict(int)
    for i in range(len(s)):
        if dict_[s[i]]:
            prev=dict_[s[i]]
            dict_[s[i]]=i+1
            answer.append(i+1-prev)
        else:
            dict_[s[i]]=i+1
            answer.append(-1)
    return answer
