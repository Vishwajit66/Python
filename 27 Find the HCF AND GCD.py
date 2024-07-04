# Find the HCF(Highe comman factor) and GCD(Greates Comman)

def findHCF(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if((x % i == 0) and (y % i == 0)):
            HCF = i
    return HCF

print("The HCF of the given two number is",findHCF(12,30))
