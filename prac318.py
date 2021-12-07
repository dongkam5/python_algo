#프로그래머스 파일명 정렬 못품

def solution(files):
    lst=[]
    for file in files:
        l=0
        r=len(file)
        for i in range(len(file)-1):
            if (not file[i].isdigit()) and file[i+1].isdigit():
                l=i+1
            if file[i].isdigit() and not file[i+1].isdigit():
                r=i+1
                break
        lst.append([file[:l],file[l:r],file[r:]])
    print(lst)
    #answer=[]
    return 0

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))