def isprime(n):
    if n == 1 or n == 2:
        return True

    for i in xrange(2, long(n**0.5)+1):
        if n % i == 0:
            return False
            exit()

    return True

counter = 0
x = 1

while counter < 10001:
    x+=1
    if isprime(x):
        counter+=1

print(counter)
print(x)
