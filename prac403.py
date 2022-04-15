# 프로그래머스 N으로 표현

def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        all_case = set()
        check_number = int(str(N)*i)
        all_case.add(check_number)

        for j in range(0, i-1):
            for x in dp[j]:
                for y in dp[-j-1]:
                    all_case.add(x+y)
                    all_case.add(x*y)
                    all_case.add(x-y)
                    if y:
                        all_case.add(x//y)
        if number in all_case:
            answer = i
            break
        dp.append(all_case)
    return answer
