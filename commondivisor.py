#common divisor
x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
if x<y:
    z=x
else:
    z=y

for i in range(1,z+1):
    if x%i==y%i==0:
        print(i,end=",")
