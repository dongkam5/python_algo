#프로그래머스 level1 추억 점수
from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    dic=defaultdict(int)
    for i in range(len(name)):
        dic[name[i]]=yearning[i]
    for list_ in photo:
        cnt=0
        for name_ in list_:
            cnt+=dic[name_]
        answer.append(cnt)
    return answer