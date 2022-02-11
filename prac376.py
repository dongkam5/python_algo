# 프로그래머스 양궁대회
from sys import setrecursionlimit

setrecursionlimit(10**6)


def Do(info, lst, n, i, diff):
    global m
    global score
    if i > 0:
        # 이기는 경우
        if info[i] == 0:
            need = 1
        else:
            need = info[i]+1
        if need <= n:
            if info[i] != 0:
                Do(info, lst+str(need), n-need, i-1, diff-i*2)
            else:
                Do(info, lst+str(need), n-need, i-1, diff-i)
        # 지는 경우
        Do(info, lst+'0', n, i-1, diff)
    elif i == 0:
        Do(info, lst+str(n), 0, i-1, diff)
    else:
        if diff < 0 and diff < score:
            score = diff
            m.clear()
            l = list(map(int, lst))
            l.reverse()
            m.append(l)
        elif diff < 0 and diff == score:
            l = list(map(int, lst))
            l.reverse()
            m.append(l)


def solution(n, info):
    global m
    global score
    score = 10000
    m = []
    answer = []
    info.reverse()
    diff = 0
    for i in range(11):
        if info[i] != 0:
            diff += i
    Do(info, '', n, 10, diff)
    if m:
        m.sort()
        answer = m[-1]
        answer.reverse()
        return answer
    else:
        return [-1]


print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
