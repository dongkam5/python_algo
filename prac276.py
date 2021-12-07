#프로그래머스 콜라스 추측
def solution(num):
    i=0
    answer = 0
    while True:
        if num==1:
            break
        elif i==500:
            answer=-1
            break
        elif num%2==0:
            i+=1
            answer+=1
            num=num//2
        elif num%2==1:
            i+=1
            answer+=1
            num=(num*3+1)
    return answer

    