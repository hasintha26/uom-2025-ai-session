sum_1=0
sum_2=0
for i in range(101):
    sum_1+=i**2
    sum_2+=i
sum_2=sum_2**2
print(sum_2-sum_1)