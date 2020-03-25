#prime number
x=int(input("Enter the number: "))
if x>1:
    for i in range(2,x//2):
        if(x%i==0):
            print(x, "is not a prime numbr.")
            break
    else:
         print(x,"is a prime number.")
else:
    print(1,"is a prime number.")
