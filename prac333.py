#프로그래머스 멀쩡한 사각형 못품
import math
def solution(w,h):
    if w>h:
        w,h=h,w
    S=w*h
    a=math.ceil(h/w)
    cnt= a*w
    answer=S-cnt
    return answer

w,h=map(int,input().split())
print(solution(w,h))
