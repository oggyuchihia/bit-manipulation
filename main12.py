def divide(divident,divisor):
    sign=(-1 if((divident<0) ^ (divisor<0)) else 1)
    divident=abs(divident)
    divisor=abs(divisor)
    quotient=0
    tempnumber=0
    for i in range(31,-1,-1):
        if(tempnumber + (divisor<<i))<=divident:
            tempnumber+=divisor<<i
            quotient|=1<<i
    if sign==-1:
        quotient=-quotient
    return quotient

a=int(input("entert the divident"))
b=int(input("entert the divisor"))
print("division is ", divide(a,b))