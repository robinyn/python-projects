def isprime(n):
    if n == 1 or n == 2:
        return True

    for i in xrange(2, long(n**0.5)+1):
        if n % i == 0:
            return False
            exit()

    return True

currentNum=long(input("Please input a number: "))

for i in xrange(1, currentNum+1):
    if currentNum%i==0:
        if isprime(i):
            print("Prime factor: {}".format(i))
        else:
            print("Non-prime factor: {}".format(i))
        #print(currentNum)
        #currentNum/=i
        #break
