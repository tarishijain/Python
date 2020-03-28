list=[1,2,3,4,3,4,8,10,2,3]
print(list)

list1=[]
while(list):
    i=list[0]
    if i not in list1:
        index=list.index(i)
        n=list.pop(index)
        list1.append(n)
        
    else:
        list.insert(0,i+1)
        list.pop(1)
        
print(list1)

