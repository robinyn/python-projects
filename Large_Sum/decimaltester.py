from decimal import *

getcontext().prec = 10

a=0.1232
b=0.0020849603

c=Decimal(a)+Decimal(b)
print(c.scaleb(c.adjusted()*-1))

#print(Decimal(a).adjusted())
#print(Decimal(a).scaleb(-1))
#print(Decimal(a).scaleb(Decimal(a).adjusted()*-1))



#print(Decimal(1)/Decimal(3))
