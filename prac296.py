#프로그래머스 키패드
def solution(numbers, hand):
    answer = ''
    left=10
    right=12
    for num in numbers:
        if num==1 or num==4 or num==7:
            answer+='L'
            left=num
        elif num==3 or num==6 or num==9:
            answer+='R'
            right=num
        else:
            if num==0:
                num=11
            l_move=abs((left-1)//3-(num-1)//3)+abs((left-1)%3-(num-1)%3)
            r_move=abs((right-1)//3-(num-1)//3)+abs((right-1)%3-(num-1)%3)
            if l_move==r_move:
                if hand=='right':
                    answer+='R'
                    right=num
                else:
                    answer+='L'
                    left=num
            elif l_move<r_move:
                answer+='L'
                left=num
            else:
                answer+='R'
                right=num

    return answer
