sumsq=0
sqsum=0

for i in range(1, 101):
    sumsq += i
    sqsum += i**2

sumsq=sumsq**2

print(sumsq-sqsum)
