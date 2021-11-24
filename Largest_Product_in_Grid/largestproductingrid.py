file = open("/Volumes/DATA/Programming/Python/Euler_Project/Largest_Product_in_Grid/numlist.txt", "r")
fileStream = file.readlines()
numMatrix=[]
sumBuffer=0
maxSum = 0

def checkSquare(x, y):
    xsum = 0
    ysum = 0
    drsum = 0
    dlsum = 0
    sum = 0

    if x+3<20 and y+3<20:
        xsum = int(numMatrix[y][x])*int(numMatrix[y][x+1])*int(numMatrix[y][x+2])*int(numMatrix[y][x+3])
        print("Current X Axis: {} {} {} {}").format(numMatrix[y][x], numMatrix[y][x+1], numMatrix[y][x+2], numMatrix[y][x+3])
        ysum = int(numMatrix[y][x])*int(numMatrix[y+1][x])*int(numMatrix[y+2][x])*int(numMatrix[y+3][x])
        print("Current Y Axis: {} {} {} {}").format(numMatrix[y][x], numMatrix[y+1][x], numMatrix[y+2][x], numMatrix[y+3][x])
        drsum = int(numMatrix[y][x])*int(numMatrix[y+1][x+1])*int(numMatrix[y+2][x+2])*int(numMatrix[y+3][x+3])
        print("Current Dr Axis: {} {} {} {}").format(numMatrix[y][x], numMatrix[y+1][x+1], numMatrix[y+2][x+2], numMatrix[y+3][x+3])
        dlsum = int(numMatrix[y+3][x])*int(numMatrix[y+2][x+1])*int(numMatrix[y+1][x+2])*int(numMatrix[y][x+3])
        print("Current Dl Axis: {} {} {} {}").format(numMatrix[y+3][x], numMatrix[y+2][x+1], numMatrix[y+1][x+2], numMatrix[y][x+3])

    else:
        if y+3>=20 and x+3<20:
            xsum = int(numMatrix[y][x])*int(numMatrix[y][x+1])*int(numMatrix[y][x+2])*int(numMatrix[y][x+3])
            print("Current X Axis: {} {} {} {}").format(numMatrix[y][x], numMatrix[y][x+1], numMatrix[y][x+2], numMatrix[y][x+3])
        if x+3>=20 and y+3<20:
            ysum = int(numMatrix[y][x])*int(numMatrix[y+1][x])*int(numMatrix[y+2][x])*int(numMatrix[y+3][x])
            print("Current Y Axis: {} {} {} {}").format(numMatrix[y][x], numMatrix[y+1][x], numMatrix[y+2][x], numMatrix[y+3][x])

    sum = xsum
    if sum<ysum:
        sum=ysum
    if sum<drsum:
        sum=drsum
    if sum<dlsum:
        sum=dlsum

    return sum

for f in fileStream:
    numMatrix.append(f.split())


for y in range(0,20):
    for x in range(0, 20):
        print("Current Coordinate [x, y] = [{}, {}]".format(x, y))
        sumBuffer = checkSquare(x,y)
        if maxSum < sumBuffer:
            maxSum = sumBuffer
            print(maxSum)

print(maxSum)
