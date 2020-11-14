#Sum square difference
sum = 0
sum1 = 0
for i in range(101):
    sum += i*i
    sum1 += i
print((sum1*sum1)-sum)