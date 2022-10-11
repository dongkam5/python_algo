# 프로그래머스 level1 성격 유형 검사하기

from collections import defaultdict


def solution(survey, choices):
    answer = ''
    lst = defaultdict(int)
    for i in range(len(choices)):
        l = list(map(str, survey[i]))
        if choices[i] == 4:
            continue
        elif choices[i] > 4:
            lst[l[1]] += (choices[i]-4)
        elif choices[i] < 4:
            lst[l[0]] += (4-choices[i])
    if lst['T'] > lst['R']:
        answer += 'T'
    else:
        answer += 'R'
    if lst['C'] >= lst['F']:
        answer += 'C'
    else:
        answer += 'F'
    if lst['J'] >= lst['M']:
        answer += 'J'
    else:
        answer += 'M'
    if lst['A'] >= lst['N']:
        answer += 'A'
    else:
        answer += 'N'
    print(lst)
    return answer


# print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
