#프로그래머스 멀쩡한 사각형 다른사람풀이
import math
def solution(w,h):
    if w>h:
        w,h=h,w
    S=w*h
    com=math.gcd(h,w)
    answer=S-(h+w-com)
    return answer
