# find the factorial of number
i = int(input("enter the number:"))
fac =1
if (i<0):
    print("please enter a positive number")
elif (i ==0):
    print(1)
else:
    while(i>0):
        fac = fac*i
        i = i-1
print(fac)
    
# using the  "for loop" 
if (i<0):
    print("please enter a positive number")
elif (i ==0):
    print(1)
else:
    for i in range(1,i+1):
        fac=fac*i
        i = i -1
print(fac)