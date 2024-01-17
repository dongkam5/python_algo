# 프로그래머스 level2 숫자 카드 나누기
def div(num):
    arr=[]
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            arr.append(i)
            arr.append(num//i)
    return arr

def solution(arrayA, arrayB):
    min_A=min(arrayA)
    min_B=min(arrayB)
    arr_A=div(min_A)
    arr_B=div(min_B)
    ans_A=[]
    ans_B=[]
    
    for ele_arr_A in arr_A:
        for val_A in arrayA:
            if val_A % ele_arr_A!=0:
                break
        else:
            ans_A.append(ele_arr_A)
    for ele_arr_B in arr_B:
        for val_B in arrayB:
            if val_B % ele_arr_B!=0:
                break
        else:
            ans_B.append(ele_arr_B)
    A_minus_B=set(ans_A)-set(ans_B)
    B_minus_A=set(ans_B)-set(ans_A)
    answer=[]
    for val in A_minus_B:
        for ele_B in arrayB:
            if ele_B % val==0:
                break
        else:
            answer.append(val)
    for val in B_minus_A:
        for ele_A in arrayA:
            if ele_A % val==0:
                break
        else:
            answer.append(val)
    
    if answer:
        return max(answer)
    else:
        return 0
