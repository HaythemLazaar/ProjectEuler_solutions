#Largest prime factor
big_num = 600851475143 
fac = 2
max = 2
def prime(x):
    primex = True 
    nb = 0
    for i in range(1,x):
        if x % i == 0:
            nb+=1
    if nb > 1 :
        primex = False
    return primex

while big_num > 1:
    if prime(fac) == True and big_num % fac == 0 :
        if fac > max :
            max = fac 
        big_num = big_num / fac 
    else:
        fac+=1
print(max)