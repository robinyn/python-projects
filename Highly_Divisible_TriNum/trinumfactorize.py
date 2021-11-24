def isprime(n):
    if n == 1 or n == 2:
        return True

    for i in xrange(2, long(n**0.5)+1):
        if n % i == 0:
            return False
            exit()

    return True

def factorize(currentNum):
    pCounter = 0
    npCounter = 0
    print("-------------------------------------------------------")
    print("Factorizing: {}\n".format(currentNum))
    for i in xrange(1, currentNum+1):
        if currentNum%i==0:
            if isprime(i):
                print("Prime factor: {}".format(i))
                pCounter+=1
            else:
                print("Non-prime factor: {}".format(i))
                npCounter+=1
            #print(currentNum)
            #currentNum/=i
            #break
    print("\nPrime factors: {} || Non-prime factors: {} || Total: {}".format(pCounter, npCounter, pCounter+npCounter))
    return pCounter+npCounter

n = input("Please set nth parameter: ")
factorize((n*(n+1))/2)

#for x in range(1, n+1):
#    factorize((x*(x+1))/2)
