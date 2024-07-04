# convert the "kilometers" to "miles"
m = 0.621371
print("1km= 0.621371mi")
n = int(input("enter the 'kilometers:"))
if n < 0:
    print("enter positive value grater than 0")
elif n>=1:
    print(n,"km is equel to ", n*m,"miles")
