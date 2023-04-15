#심슨 룰
import math
def f(x): 
    return math.sqrt(x)

def simpson(interval,partition_num):
    start,end=interval
    result=0
    dx=(end-start)/partition_num #dx 구함
    for i in range(0,partition_num,2):
        result+=(dx)*(f(start+(i+2)*dx)+4*f(start+(i+1)*dx)+f(start+i*dx))/3 #심슨 공식 사용
    return result

print(simpson([0,2],1000))