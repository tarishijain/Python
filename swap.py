#swap two numbers
x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
print("Before swapping")
print("value of x:",x, "and y:",y)
x=x+y
y=x-y
x=x-y
print("After swapping:")
print("value of x:",x, "and y:",y)