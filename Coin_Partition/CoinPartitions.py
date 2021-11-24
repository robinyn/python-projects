conditionArr = [0, 1, 2, 5, 10, 20, 50, 100, 200]
counter = 0
anticounter = 0

def partition(number):
    n=number
    coefArr=[1 for i in range(0, n)]
    k=n

    print(coefArr)

    while k != 0 and coefArr[0]!=n:
        x=coefArr[k-1]-1
        y=coefArr[k-2]+1
        while y <= x:
            coefArr[k-2]=y
            coefArr[k-1]=x
            #print(k)
            #print("inner loop")
            #yield(coefArr[:k])
            x-=y
            k+=1
            #y+=1
        coefArr[k-2]=x+y
        #coefArr[k-1]=0
        #x = x + y - 1
        k-=1
        #print(k)
        yield(coefArr[:k])

counter=sum(1 for i in partition(200))
#for i in gen:
#    counter+=1
#    print(counter)
    #print(i)
    #for x in i:
    #    if x not in conditionArr:
#           print("not allowed")
    #        anticounter+=1
    #        break
print(counter+1)
