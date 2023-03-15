# 프로그래머스 level1 개인정보 수집 유효기간
from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    today=list(map(int,today.split('.')))
    today_year=today[0]
    today_month=today[1]
    today_day=today[2]
    today_days=today_year*12*28+today_month*28+today_day
    types=defaultdict(int)
    for term in terms:
        contract_type,contract_month=map(str,term.split())
        types[contract_type]=int(contract_month)
    for i in range(len(privacies)):
        privacy=privacies[i]
        privacy_date,privacy_type=map(str,privacy.split())
        privacy_year,privacy_month,privacy_day=map(int,privacy_date.split('.'))
        privacy_days=privacy_day+privacy_month*28+privacy_year*12*28+types[privacy_type]*28
        print(privacy_year,privacy_month,privacy_day,types[privacy_type])
        if privacy_days<=today_days:
            answer.append(i+1)
    return answer

# print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))