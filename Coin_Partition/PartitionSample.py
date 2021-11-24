def accel_asc(n):
    counter = 0
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        #print("loop k != 0")
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            #print("loop 2*x <= y")
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            #print("loop x <= y")
            print(k)
            a[k] = x
            a[l] = y
            #print("yield1")
            yield a[:k + 2]
            counter+=1
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        #print("yield2")
        print(k)
        yield a[:k + 1]
        counter+=1
    #return counter

sortgen = accel_asc(6)
counter = 0
for i in sortgen:
    print(i)
#    counter +=1

print(sortgen)
