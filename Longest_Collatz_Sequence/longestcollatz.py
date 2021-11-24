n=2
np=1
cp=0
nmax=0
while n<1000000:
    np=n
    counter=0
    while n>0 and n!=1:
        counter+=1
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
    if counter>cp:
        cp=counter
        nmax=np
    print("next:{}".format(np+1))
    n=np+1

print(cp)
print(nmax)
