
lower = int(input("enter the lonwer number:"))

upper = int(input("enter the upper number:"))



for num in range(lower,upper+1):
    order = len(str(num))
    temp = num
    sum=0
    while(temp>0):
        digit = temp % 10
        sum = sum + digit ** order
        temp = temp // 10
    if ( sum==num):
        print(num)
    