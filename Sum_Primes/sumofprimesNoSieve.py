def isprime(n):
    if n == 1 or n == 2:
        return True

    for i in xrange(2, long(n**0.5)+1):
        if n % i == 0:
            return False
            exit()

    return True

sum = 0

for x in range(2, 2000001):
    if isprime(x):
        sum+=x

print(sum)

#142913977858
