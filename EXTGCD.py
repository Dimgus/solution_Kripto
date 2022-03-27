from math import gcd


def extGCD(a,b):
    if a==0:
        return b,0,1
    else:
        gcd, x, y = extGCD(b%a,a)
        return gcd, y-(b//a)*x,x
print(extGCD(26513,32321))