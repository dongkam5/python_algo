#프로그래머스 3진법 뒤집기

def solution(n):
    lst=[]
    def tri (num):
        while num!=0:
            lst.append(str(num%3))
            num//=3
    tri(n)
    answer = int(''.join(lst),3)
    return answer

''' 다른사람 풀이
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
'''