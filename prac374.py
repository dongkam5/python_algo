# 프로그래머스 k진수웨서 소수 개수 구하기
def isprime(v):
    for i in range(2, int(v**0.5)+1):
        if v % i == 0:
            return False

    return True


def solution(n, k):
    answer = 0
    knum = ''
    while (n != 0):
        num = n % k
        n = n//k
        knum += str(num)
    knum = knum[::-1]
    lst = []
    curr = ''
    for i in range(len(knum)):
        if knum[i] == '0' and curr != '':
            lst.append(curr)
            curr = ''
        elif knum[i] != '0':
            curr += knum[i]
    if curr != '':
        lst.append(curr)
    for n in lst:
        n = int(n)
        if n > 1 and isprime(n):
            answer += 1
    return answer


# print(solution(437674, 3))
print(solution(110011, 10))
