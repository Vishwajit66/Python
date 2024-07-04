# Number divisible by another Number

# Using for Loop 

"""print("this number is divisible by 13:")

for i in range (1,100):
    if  i % 13 == 0:
         print(i)
"""

# Using Lambda funtion and filiter funtion on area

l = [39,38,26,98,33,67,87]

result = list(filter(lambda x : x%13 ==0,l))
print("this are the number is divisible by 13",result)

