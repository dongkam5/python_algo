# 프로그래머스 주차 요금 계산
def solution(fees, records):
    answer = []
    book = {}
    carSpend = {}
    cars = []
    stdTime, stdFee, overTime, overFee = map(int, fees)
    for record in records:
        time, num, action = map(str, record.split())
        carSpend[num] = 0
    for record in records:
        time, num, action = map(str, record.split())
        if action == 'OUT':
            outHour, outMin = time.split(':')
            outTime = int(outHour)*60+int(outMin)
            spend = outTime-book[num]
            carSpend[num] += spend
            book[num] = -1

        else:
            inHour, inMin = time.split(':')
            inTime = int(inHour)*60+int(inMin)
            book[num] = inTime
    if book:
        outTime = 23*60+59
        for num in book:
            if book[num] != -1:
                spend = outTime-book[num]
                carSpend[num] += spend
                book[num] = -1
    for car in carSpend:
        if carSpend[car] > stdTime:
            if (carSpend[car]-stdTime) % overTime == 0:
                bill = stdFee+((carSpend[car]-stdTime)//overTime)*overFee
            else:
                bill = stdFee + \
                    ((carSpend[car]-stdTime)//overTime+1)*overFee
        else:
            bill = stdFee
        cars.append([car, bill])
    cars.sort()
    for car in cars:
        answer.append(car[1])
    return answer
