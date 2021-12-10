#프로그래머스  위장
def solution(clothes):
    answer = 1
    lst={}
    for clothe in clothes:
        if clothe[1] in lst:
            lst[clothe[1]]+=1
        else:
            lst[clothe[1]]=1
    for val in lst.values():
        answer*=(val+1)
    return (answer-1)

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))