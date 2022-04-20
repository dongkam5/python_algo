# 프로그래머스 [1차] 셔틀버스

from collections import deque


def solution(n, t, m, timetable):
    answer = ''
    bus_time = []
    bus_cnt = [[] for _ in range(n)]
    for i in range(n):
        bus_time.append(540+i*t)
    for i in range(len(timetable)):
        a, b = map(int, timetable[i].split(':'))
        timetable[i] = a*60+b
    timetable.sort()
    i = 0
    j = 0
    cnt = 0
    while i < len(timetable) and j < n:
        if timetable[i] <= bus_time[j]:
            cnt += 1
            bus_cnt[j].append(timetable[i])
            if cnt == m:
                cnt = 0
                j += 1
        else:
            while j < n:
                if timetable[i] <= bus_time[j]:
                    break
                j += 1
            cnt = 1
            if j < n:
                bus_cnt[j].append(timetable[i])
        i += 1
    print(timetable)
    print(bus_time)
    print(bus_cnt)
    if len(bus_cnt[n-1]) != m:
        answer = bus_time[n-1]
    else:
        answer = bus_cnt[n-1][m-1]-1
    H = answer//60
    M = answer % 60
    answer = str(H).rjust(2, '0')+':'+str(M).rjust(2, '0')
    return answer


# print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
# print(solution(2,	1, 2, ["09:00", "09:00", "09:00", "09:00"]))
# print(solution(1,	1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
# print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 25, 1, ["09:00", "09:10", "09:20", "09:30", "09:40",
      "09:50", "10:00", "10:10", "10:20", "10:30", "10:40", "10:50"]))
