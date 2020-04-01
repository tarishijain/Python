dict1={"student1":"Aman","student2":"Dheeraj","student3":"Mohit","student4":"Kanika","student5":"Amrita"}
print(dict1)
list1=[]
for i in dict1:
    list1.append(dict1[i])
list1.sort()
c = dict(zip(dict1.keys(),list1)) #to convert lists to dict. 
print(c) 
