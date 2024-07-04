# check the large number in between 3 number
f = int(input("enter the number 1st number"))
s = int(input("enter the number 2nd number"))
t = int(input("enter the number 3rd number"))
print("it is large number",max(f,s,t))

if (f>s) and (f>t):
    print(f,"is large number ")
    
elif(f<s) and (s>t):
    print(s,"is large number ")

elif(f<t) and (t>s):
    print(t,"is large number ")
    