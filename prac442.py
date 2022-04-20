# 프로그래머스 보석 쇼핑

def find_m_gem(jew):
    min_ = 1000000
    for gem in jew:
        if min_ > jew[gem]:
            min_ = jew[gem]
            m_gem = gem
    return m_gem


def solution(gems):
    answer = [-1, -1]
    jew = {}
    kinds = len(set(gems))
    for i in range(len(gems)):
        jew[gems[i]] = i
        if len(jew) == kinds:
            m = min(jew.values())
            diff = i-m
            answer[0] = m+1
            answer[1] = i+1
            i += 1
            break
    m_gem = find_m_gem(jew)
    while i < len(gems):
        if m_gem == gems[i]:
            jew[gems[i]] = i
            m_gem = find_m_gem(jew)
        else:
            jew[gems[i]] = i
        m = jew[m_gem]
        if i-m < diff:
            answer[0] = m+1
            answer[1] = i+1
            diff = i-m
        i += 1
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA",
      "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
