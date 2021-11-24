file = open("/Volumes/DATA/Programming/Python/Euler_Project/Maximum_Path_Sum/data.txt", "r")
fileStream=file.readlines()
temp=[]
row=1

for f in fileStream:
    temp.append(f.split())

#for i in range(0, 15):
#    x=0
#    while x in range(0, len(temp[i])):
#
#        x+=1

while row < 14:
    x=0
    while x in range(0, len(temp[row+1])):
        
