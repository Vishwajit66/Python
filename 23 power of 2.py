# Display the power of 2 using anonymous(Lambda Funtion) Funtions.

n = int(input("Enter the number of terms here:"))

result  = list (map(lambda x : 2 ** x,  range(n+1)))

for i in range (n+1):
    print("the valude of 2 raised to power",i,"is",result[i])
