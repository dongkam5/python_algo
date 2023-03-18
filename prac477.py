#프로그래머스 level1 둘만의 암호
def solution(s, skip, index):
    answer = ''
    skip_ord=[] # skip알파벳의 아스키코드 번호 저장
    for skip_alpha in skip:
        skip_ord.append(ord(skip_alpha)) # skip의 문자열을 아스키코드로 변환 후 skip_ord에 추가
    for val in s: # 각 문자열에 대해서
        i=index
        order=ord(val) #문자열의 아스키코드를 order로 받음
        while i>0: 
            order+=1
            if ord('z')<order: # 아스키코드값이 ord('z')를 초과하면, 'a'로 변환
                order-=26
            if order in skip_ord:
                continue
            i-=1 # skip에 문자열이 없는 경우에만 i 감소
        answer+=chr(order)
    return answer