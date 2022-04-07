# 프로그래머스 입국심사 실패
def solution(n, times):
    answer = 0
    start = 1
    end = max(times)*n
    while True:
        mid = (start+end)//2
        cnt = 0
        for time in times:
            cnt += mid//time
        if cnt == n:
            end = mid
            start = mid//2
            while True:
                mid = (start+end)//2
                if start == mid or end == mid:
                    break
                cnt = 0
                for time in times:
                    cnt += mid//time
                if cnt < n:
                    start = mid
                else:
                    end = mid
            break
        elif cnt > n:
            if cnt//n >= 2:
                end = (end//(cnt//n))
            else:
                end = mid
        elif cnt < n:
            if n//cnt >= 2:
                start = (start*(n//cnt))
            else:
                start = mid
    answer = mid+1
    return answer


print(solution(6, [7, 10]))
