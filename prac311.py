#프로그래머스 124나라의 숫자
def solution(n):
    answer = ''
    n-=1
    nums={0:'1',1:'2',2:'4'}
    while n>=0:
        answer+=nums[n%3]
        n=(n//3-1)
    return answer[::-1]

n=int(input())
print(solution(n))

'''다른사람풀이
def change124(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer
'''

