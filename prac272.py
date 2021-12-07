#프로그래머스 같은 숫자는 싫어
def solution(arr):
    answer = []
    arr.append(100)
    i=0
    while i<len(arr)-1:
        if arr[i]!=arr[i+1]:
            answer.append(arr[i])
        i+=1
    return answer

print(solution([1,1,3,3,0,1,1]))