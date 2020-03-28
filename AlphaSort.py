dict={"student1":"Aman","student2":"Dheeraj","student3":"Mohit","student4":"Kanika","student5":"Amrita"}
list1=[]
list2=[]
for key,value in dict.items():
    list1.append(key)
    list2.append(value)
list2.sort()
dict1={}
for x in list1:
    for y in list2:
        dict1[x]=y
        list2.remove(y)
        break


print(dict1)    

