#프로그래머스 [3차] 파일명 정렬
def solution(files):
    answer = []
    lst=[]
    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                break
        for j in range(5):
            if (i+j)<len(file) and file[i+j].isdigit():
                continue
            else:
                j+=i
                break
        else:
            j=i+5
        s=[file[:i],file[i:j],file[j:]]
        lst.append(s)
    lst.sort(key=lambda x:(x[0].upper(),int(x[1])))
    for val in lst:
        answer.append(''.join(val))
    return answer