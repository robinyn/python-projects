def factorial(num):
    buffer = num
    if num>1:
        buffer*=factorial(num-1)
    return buffer

print(str(factorial(40)/(factorial(20)*factorial(20))))
