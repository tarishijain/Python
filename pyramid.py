n=int(input("Enter no of rows: "))

for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    print("* "*i)    
    print("\r")

                       