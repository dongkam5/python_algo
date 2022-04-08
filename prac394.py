# 프로그래머스 디스크 컨트롤
def solution(jobs):
    answer = 0
    schedule = []
    jobs.sort()
    length = len(jobs)
    end = 0
    while jobs:
        if schedule:
            start, spend = schedule.pop()
            answer += (spend+end-start)
            end += spend
        else:
            start, spend = jobs.pop(0)
            answer += spend
            end = start+spend
        while jobs and jobs[0][0] <= end:
            schedule.append(jobs.pop(0))
        schedule.sort(key=lambda x: -x[1])
    schedule.sort(key=lambda x: -x[1])
    while schedule:
        start, spend = schedule.pop()
        answer += (spend+end-start)
        end += spend
    answer = answer//length
    return answer


print(solution([[1, 1], [1, 2], [1, 3]]))
