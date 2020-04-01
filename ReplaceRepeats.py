list1=[1,2,3,4,3,4,8,10,2,3]
print(list1)
N='rep'
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        list2.append(N)
print(list2)
