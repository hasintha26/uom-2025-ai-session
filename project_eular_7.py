def isprime(num):
    if num ==1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
prime_list=[]
n=2
while len(prime_list)<10001:
    if isprime(n):
        prime_list.append(n)
    n+=1
print(prime_list[-1])