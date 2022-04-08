# 프로그래머스 섬 연결하기

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    island = {}
    cnt = 0
    for i in range(n):
        island[i] = 0
    a, b, c = costs.pop(0)
    island[a] += 1
    island[b] += 1
    answer += c
    cnt += 1
    while cnt != n-1:
        for i in range(len(costs)):
            a, b, c = costs[i]
            if island[a] >= 1 and island[b] >= 1:
                continue
            elif island[a] >= 1 and island[b] < 1:
                island[a] += 1
                island[b] += 1
                answer += c
                cnt += 1
                costs.pop(i)
                break
            elif island[a] < 1 and island[b] >= 1:
                island[a] += 1
                island[b] += 1
                answer += c
                cnt += 1
                costs.pop(i)
                break
    return answer
