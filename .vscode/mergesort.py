def merge_sort (lst):
    ans=[]
    mid=len(lst)//2
    if len(lst)<=1:
        return lst
    g1=merge_sort(lst[:mid])
    g2=merge_sort(lst[mid:])
    while g1 and g2:
        if g1[0]<g2[0]:
            ans.append(g1.pop(0))
        else:
            ans.append(g2.pop(0))
    while g1:
        ans.append(g1.pop(0))
    while g2:
        ans.append(g2.pop(0))
    return ans
n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
lst=merge_sort(lst)
for i in range(n):
    print(lst[i])