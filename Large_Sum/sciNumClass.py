from decimal import *

getcontext().prec=11

class sciNum:
    def __init__(self, inputVal, inputMag):
        self.value=Decimal(inputVal)
        self.magnitude=inputMag
        sciNum.scify(self)
#        length = len(str(int(inputVal)))
#        magFactor = 0
#        if length>1:
#            magFactor=length-1
#            self.value=inputVal/10**magFactor
#            self.magnitude=inputMag+magFactor
#        else:
#            self.value=inputVal
#            self.magnitude=inputMag

    def change_Val(self, value):
        self.value = Decimal(value)

    def change_Magnitude(self, magnitude):
        self.magnitude = magnitude

    def printSci(self):
        print("{} e^{}".format(self.value, self.magnitude))

    def scify(self):
        #length = len(str(int(self.value)))
        #magFactor = 0
        #if length>1:
        #    magFactor=length-1
        #    self.value/=10**magFactor
        #    self.magnitude+=magFactor
        magFactor=Decimal(self.value).adjusted()*-1
        self.value=Decimal(self.value).scaleb(magFactor)
        self.magnitude-=magFactor

    def matchMag(num1, num2):
        magFactor = num1.magnitude - num2.magnitude
        if magFactor == 0:
            return
        elif magFactor > 0:
            num2.value/=10**abs(magFactor)
            num2.magnitude+=abs(magFactor)
        elif magFactor < 0:
            num1.value/=10**abs(magFactor)
            num1.magnitude+=abs(magFactor)

    def addition(self, num1):
        sciNum.matchMag(self, num1)
        self.value+=num1.value
        self.magnitude=num1.magnitude
        sciNum.scify(self)

    def subtraction(self, num1):
        sciNum.matchMag(self, num1)
        self.value-=num1.value
        self.magnitude=num1.magnitude
        sciNum.scify(self)

    def multiplication(self, num1):
        self.value*=num1.value
        self.magnitude+=num2.magnitude
        sciNum.scify(self)

    def division(self, num1):
        self.value/=num1.value
        self.magnitude-=num1.magnitude
        sciNum.scify(self)
