def ispalindrome(n):
    for i in range(0, (len(n)//2)+1):
        if n[i] != n[len(n)-1-i]:
            return False
    return True

buffer = 0

for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        if ispalindrome(str(x*y)) and buffer<(x*y):
            buffer=x*y

print(buffer)
