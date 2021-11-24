def isprime(n):
    if n == 1 or n == 2:
        return True

    for i in xrange(2, long(n**0.5)+1):
        print(i)
        if n % i == 0:
            return False
            exit()

    return True

inputNum = input("Please input a number: ")

for x in xrange(inputNum, 1, -1):
    print(x)
    if inputNum % x == 0:
        print("Testing factor: {}".format(x))
        if isprime(x):
            print("The largest prime factor of {} is {}".format(inputNum, x))
            exit()
        else:
            print("Not prime")
