def ispalindromic(list):
    if list==list[::-1]:
        return True 
    return False
max_palindromic=0
for i in range(100,1000):
    for j in range(100,1000):
        mul=i*j
        if ispalindromic(str(mul)):
            if mul>max_palindromic:
                max_palindromic=mul
print(max_palindromic)