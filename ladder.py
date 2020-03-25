n=int(input("Enter no. of ladders:"))
l=n*3+2
for j in range(1,l+1):
    if j%3==0:
        print("*"*5)
    else:
        print("*   *")    
