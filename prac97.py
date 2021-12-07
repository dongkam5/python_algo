#백준 1543
lst=input()
s=input()
check=0
i=0
while i<(len(lst)-len(s)+1):
    if lst[i:i+len(s)]==s:
        check+=1
        i=i+len(s)
    else:
        i+=1
print(check)