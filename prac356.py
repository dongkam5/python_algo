#프로그래머스 전화번호 목록
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        leng1=len(phone_book[i])
        leng2=len(phone_book[i+1])
        if leng1<leng2 and phone_book[i]==phone_book[i+1][:leng1]:
            return False
    return True

