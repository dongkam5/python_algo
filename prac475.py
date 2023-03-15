#프로그래머스 level1 대충 만든 자판
from collections import defaultdict
def solution(keymap, targets):
    answer = []
    best=defaultdict(int)
    for key in keymap:
        for i in range(len(key)):
            if best[key[i]]==0:
                best[key[i]]=i+1
            else:
                if best[key[i]]>i+1:
                    best[key[i]]=i+1
    for target in targets:
        temp=0
        for t in target:
            if best[t]==0:
                temp=0
                break
            else:
                temp+=best[t]
        if temp==0:
            answer.append(-1)
        else:
            answer.append(temp)
    return answer

# print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))
# print(solution(['AA'],['A']))