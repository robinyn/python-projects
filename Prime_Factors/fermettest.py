inputNum = input("Please input a long integer: ")

for i in xrange(2, inputNum/100000):
    print(i)
    if (i**(inputNum-1))%inputNum != 1:
        print("Not prime")
        exit()

print("Prime")
