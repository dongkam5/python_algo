#프로그래머스 level2 이진수 문제
bit=[1,0,1,0,0]

print(bit.index(0))

bit.reverse()
zeroind=bit.index(0)
oneind=bit.index(1,0,zeroind)
print(len(bit)-1-zeroind)
print(oneind)