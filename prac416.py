# 프로그래머스 가장 긴 펠린드롬
from collections import deque


def solution(s):
    answer = 0
    for i in range(len(s)):
        pel = []
        stack = []
        cnt = 0
        for j in range(i, len(s)):
            val = s[j]
            if len(stack) >= 1:
                if len(stack) == 1:
                    if val == stack[-1]:
                        cnt += 2
                        stack.pop()
                        pel.append(val)
                        pel.append(val)
                    else:
                        stack.append(val)
                        cnt = 0
                elif len(stack) >= 2:
                    if val == stack[-2]:
                        cnt += 3
                        pel.append(val)
                        pel.append(stack.pop())
                        pel.append(stack.pop())
                    elif val == stack[-1]:
                        cnt += 2
                        stack.pop()
                        pel.append(val)
                        pel.append(val)
                    else:
                        stack.append(val)
                        cnt = 0
                if len(pel) > 1:
                    mid = len(pel)//2
                    check = 0
                    for i in range(mid):
                        if pel[i] == pel[len(pel)-1-i]:
                            continue
                        else:
                            check = 1
                            break
                    if check == 0:
                        answer = max(answer, len(pel))
                    else:
                        pel.clear()
            else:
                stack.append(val)
                cnt = 0
            answer = max(cnt, answer)
        if stack:
            pel.append(stack.pop())
            if len(pel) > 1:
                mid = len(pel)//2
                check = 0
                for i in range(mid):
                    if pel[i] == pel[len(pel)-1-i]:
                        continue
                    else:
                        check = 1
                        break
                if check == 0:
                    answer = max(answer, len(pel))
                else:
                    pel.clear()

    return answer


print(solution('aabaa'))
