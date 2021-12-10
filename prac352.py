#프로그래머스 카펫
def solution(brown, yellow):
    for h in range(1,yellow+1):
        if yellow%h==0:
            w=yellow//h
            if w<h:
                break
            if (w+2)*2+2*h==brown:
                return [w+2,h+2]