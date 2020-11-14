#Smallest multiple that can be divided by numbers from 1 to 20

x = 2520
dv = 1
while dv < 21 :
    if x % dv == 0 :
        dv += 1
    else :
        print(dv)
        dv = 1
        x += 2520
print(x)