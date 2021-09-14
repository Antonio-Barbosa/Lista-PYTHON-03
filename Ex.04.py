n=int(input('N: '))
a,b = 1,1
cont = 1
while cont <= n-2:
    a,b = b, a+b
    cont= cont + 1
print (b)
