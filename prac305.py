#프로그래머스 최솟값 만들기

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer+=(A[i]*B[i])
    return answer

'''다른사람풀이
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
'''