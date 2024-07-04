#Display fibonacci Swquence Using Recursion

def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2)) 
    
n = int(input("Enter the number of terms: "))
if n <= 0 :
    print("enter positive number")
else:
    print("finbonacci sequence")
    for i in range(n):
        print(fibo(i))