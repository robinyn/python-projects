currentNum=long(input("Please input a number: "))

while currentNum != 1:
    for i in xrange(2, currentNum+1):
        if currentNum%i==0:
            print("Prime factor: {}".format(i))
            #print(currentNum)
            currentNum/=i
            break
