#프로그래머스 핸드폰 번호 가리기
def solution(phone_number):
    lst=list(map(str,phone_number))
    for i in range(len(phone_number)-4):
        lst[i]='*'
    answer = ''.join(lst)
    return answer

print(solution('01033334444'))