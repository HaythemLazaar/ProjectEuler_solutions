#Palindrome number
x = 10000
max = 0
def palindrome(y):
    pal = False
    if y / 100000 >= 1:
        if y % 10 == int(x/100000):
            if ((y%100)-(y%10))==int(x/10000)%10 :
                if int((y%1000)/100)==int(y/1000)%10:
                    pal = True
    else:
        if int(y/10000)==y%10:
            if int(y/1000)%10==(y%100)-(y%10):
                pal = True
    return pal
print(palindrome(900009))
while x < 998001:
    for i1 in range(99,1000):
        for i2 in range(99,1000):
            x = i1 * i2
            if palindrome(x) == True and x > max:
                max = x
print(max)