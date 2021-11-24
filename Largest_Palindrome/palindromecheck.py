def ispalindrome(n):
    for i in range(0, (len(n)//2)+1):
        if n[i] != n[len(n)-1-i]:
            return False
    return True

x = raw_input()
print(ispalindrome(x))
