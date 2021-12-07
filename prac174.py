#프로그래머스 순간이동 다른풀이
def solution(n):
    cnt = 0
    while n > 0:
        q, r = divmod(n, 2)
        n = q
        if r != 0:
            cnt += 1
    return cnt
''' 다른풀이
def solution(n):
    return len([i for i in bin(n)[2:] if i == '1'])
'''
