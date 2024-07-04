# Display the sum of natural number usin recursion

def SON():
    if n <= 1:
        return n
    else:
        return n + SON(n-1) 
    
n = int(input("Enter the number:"))

if n <= 0 :
    print("enter positive number")
else:
    print("sum of natural number",SON(n))
