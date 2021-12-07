#프로그래머스 2개 이하로 다른 비트 시간초과
def solution(numbers):
    answer = []
    for number in numbers:
        b=bin(number)[2:]
        k=(number+1)
        while True:
            b_=bin(k)[2:]
            cross=[0]*(len(b_))
            d=len(b_)-len(b)
            for i in range(len(b)):
                if b[i]==b_[d+i]:
                    cross[i]=0
                else:
                    cross[i]=1
            for i in range(d):
                cross.append(1)
            if 1<=cross.count(1)<=2:
                answer.append(k)
                break
            k+=1
    return answer
