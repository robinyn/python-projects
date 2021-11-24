currentNum=2
buffer = 1
factorArr=[0 for y in range(0,20)]
tempArr=[0 for y in range(0,20)]

for currentNum in range(2, 21):
    print("Current: " + str(currentNum))
    while currentNum != 1:
        for i in xrange(2, currentNum+1):
            if currentNum%i==0:
                tempArr[i-1]+=1
                currentNum/=i
                break
    for g in range(0, 20):
        if tempArr[g]>factorArr[g]:
            factorArr[g]=tempArr[g]
        tempArr[g]=0


for g in range(0, 20):
    buffer *= (g+1)**factorArr[g]

print(factorArr)
print(buffer)
