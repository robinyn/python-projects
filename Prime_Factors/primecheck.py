inputNum = input("Please enter a number to check: ")

if inputNum == 1 or inputNum == 2:
    print("prime")

for i in range(2, int(inputNum**0.5)+1):
    if inputNum % i == 0:
        print("not prime")
        exit()

print("prime")
