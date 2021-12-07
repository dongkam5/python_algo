#프로그래머스 [1차] 비밀지도
from collections import deque
def solution(n, arr1, arr2):
    answer = []
    field1=deque([])
    field2=deque([])
    for i in range(n):
        field1.append(deque(map(str,bin(arr1[i]))))
        field2.append(deque(map(str,bin(arr2[i]))))
        field1[i].popleft()
        field1[i].popleft()
        field2[i].popleft()
        field2[i].popleft()
        while len(field1[i])!=n:
            field1[i].appendleft('0')
        while (len(field2[i]))!=n:
            field2[i].appendleft('0')
    for i in range(n):
        s=[]
        for j in range(n):
            if int(field1[i][j])+int(field2[i][j])>0:
                s.append('#')
            else:
                s.append(' ')
        answer.append(''.join(s))
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))