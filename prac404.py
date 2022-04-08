# 프로그래머스 여행경로

def solution(tickets):
    global answer
    answer = []
    fromto = {}
    manage_ticket = {}
    temp = []
    for ticket in tickets:
        dep, arr = ticket
        manage_ticket[dep+arr] = 0
        fromto[dep] = []
        fromto[arr] = []
    for ticket in tickets:
        dep, arr = ticket
        fromto[dep].append(arr)
        manage_ticket[dep+arr] += 1
    for dep in fromto.keys():
        fromto[dep].sort()
    print(fromto)

    def dfs(dep):
        global answer
        if len(temp) == len(tickets)+1:
            if not answer:
                answer = list(map(str, temp))
        else:
            if fromto[dep]:
                for arr in fromto[dep]:
                    if manage_ticket[dep+arr] >= 1:
                        temp.append(arr)
                        manage_ticket[dep+arr] -= 1
                        dfs(arr)
                        temp.pop()
                        manage_ticket[dep+arr] += 1
    temp.append("ICN")
    dfs("ICN")
    return answer


print(solution([["ICN", "AAA"], ["ICN", "AAA"], [
      "ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]))
