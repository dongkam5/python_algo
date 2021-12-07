#프로그래머스 가장 큰 수
def solution(numbers):
    numbers=list(map(str,numbers))
    numbers.sort(reverse=True)
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            small_len=min(len(numbers[i]),len(numbers[j]))
            for k in range(small_len):
                if int(numbers[i][k])<int(numbers[j][k]):
                    numbers[i],numbers[j] = numbers[j] , numbers[i]
            else:
                if len(numbers[i])<len(numbers[j]):
                    if int(numbers[i][k])<int(numbers[j][k+1]):
                        numbers[i],numbers[j]=numbers[j],numbers[i]
                elif len(numbers[i])>len(numbers[j]):
                    if int(numbers[i][k+1])<int(numbers[j][k]):
                        numbers[i],numbers[j]=numbers[j],numbers[i]
    return ''.join(numbers)

print(solution([3, 30, 34, 5, 9]))