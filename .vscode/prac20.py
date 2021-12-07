def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True
while True:
    n=int(input())
    if n==0:
        break
    for i in range(3,n//2+1):
        if isPrime(i) and isPrime(n-i):
            print("{} = {}+{}".format(n,i,n-i))
            break
        elif i==(n//2):
            print("Goldbach's conjecture is wrong.")