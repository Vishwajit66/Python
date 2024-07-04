#Chenk the loop year
n= int(input("enter year:"))
if (n%400==0) and (n%100==0):
    print("it is loop year")
elif(n%4==0) and (n%100!=0):
    print("it is loop year")
else:
    print("it is not loop year")
