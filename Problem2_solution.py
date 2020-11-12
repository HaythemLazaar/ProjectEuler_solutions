#Fibonnaci Sequence
term1 = 1 
term2 = 2
sum = 2
while term2 < 4000000 : 
    aux = term1
    term1 = term2
    term2 = aux + term2
    if term2 % 2 == 0:
        sum+= term2
print(sum)