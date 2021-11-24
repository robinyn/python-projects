def isprime(n):
    if n == 1 or n == 2:
        return True

    for i in xrange(2, long(n**0.5)+1):
        if n % i == 0:
            return False
            exit()

    return True

sieve = [True for x in range(0,2000001)]
sum = 0

for x in range(2, 2000001):
    if isprime(x):
        print(x)
        y=2
        while x*y<2000000:
            sieve[x*y]=False
            y+=1

for z in range(0, 2000000):
    if sieve[z]:
        print("add")
        sum+=(z+1)

print(sum)
