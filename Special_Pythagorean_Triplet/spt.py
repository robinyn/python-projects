#for a in range(1, 1000):
#    for b in range(1, 1000):
#        for c in range(1, 1000):
#            if(a+b+c)==1000:
#                print("{} {} {}".format(a, b, c))
#                if (c**2)==(a**2+b**2):
#                    print(a*b*c)

def is_square(n):
    sqrt = int(n**0.5)
    return sqrt-(n**0.5)==0

for a in range(1, 1000):
    for b in range(1, 1000):
        c=(a**2)+(b**2)
        if is_square(c)and a+b+(c**0.5)==1000:
             print("{} {} {}".format(a, b, (c**0.5)))
             print(a*b*(c**0.5))
             exit()
