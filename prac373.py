# 프로그래머스 신고결과받기
def solution(id_list, report, k):
    answer = []
    ban = {}
    mail = {}
    for id in id_list:
        ban[id] = ''
        mail[id] = 0
    report = list(set(report))
    for re in report:
        a, b = re.split()
        ban[b] += a+' '
    for id in id_list:
        l = list(map(str, ban[id].split()))
        if(len(l) >= k):
            for name in l:
                mail[name] += 1
    for val in mail:
        answer.append(mail[val])
    return answer
