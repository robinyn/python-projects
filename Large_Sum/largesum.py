from decimal import *

getcontext().prec=11

class sciNum:
    def __init__(self, inputVal, inputMag):
        self.value=Decimal(inputVal)
        self.magnitude=inputMag
        sciNum.scify(self)

    def change_Val(self, value):
        self.value = Decimal(value)

    def change_Magnitude(self, magnitude):
        self.magnitude = magnitude

    def printSci(self):
        print("{} e^{}".format(self.value, self.magnitude))

    def scify(self):
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

file = open("/Volumes/DATA/Programming/Python/Euler_Project/Large_Sum/numbers.txt", "r")
numberArray = file.read().splitlines()
calcArray=[]
result=sciNum(0,0)

for digit in range(49, -1, -1):
    sum=0
    for number in range(0,100):
        sum+=int(numberArray[number][digit])
    calcArray.append(sciNum(Decimal(sum), 50-(digit+1)))

for x in range(0, 50):
    calcArray[x].printSci()
    result.addition(calcArray[x])

result.printSci()
