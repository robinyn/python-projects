n=200
coefArr=[1 for i in range(0, n)]
k=n
counter = 0

print(coefArr)
while k != 0 and coefArr[0]!=n:
    x=coefArr[k-1]-1
    y=coefArr[k-2]+1
    while y <= x:
        coefArr[k-2]=y
        coefArr[k-1]=x
        print(coefArr)
        counter+=1
        y+=1
        x-=1
    coefArr[k-2]=x+y
    coefArr[k-1]=0
    k-=1
    print(coefArr)
    counter+=1

print(counter)
