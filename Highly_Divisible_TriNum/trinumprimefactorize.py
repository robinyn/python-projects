def pfactorize(currentNum):
    prevNum=2
    counter=0
    operator=1
    while currentNum != 1:
        for i in xrange(2, currentNum+1):
            if currentNum%i==0:
                if prevNum==i:
                    counter+=1
                else:
                    operator*=(counter+1)
                    counter=1
                prevNum=i
                currentNum/=i
                break

    operator*=(counter+1)

    return operator

r=0
x=0
while r<500:
    x+=1
    r = pfactorize((x*(x+1))/2)
    print("Testing x:{} r:{}".format(x, r))
print("{}th Triangular Number: {} has {} factors".format(x, ((x*(x+1))/2), r))
