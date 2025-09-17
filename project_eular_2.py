frist=1
second=1
fib_no=0
sum=0
while  fib_no<4000000:
    fib_no=frist+second
    frist=second
    second=fib_no
    if fib_no%2==0:
        sum+=fib_no
print(sum)
