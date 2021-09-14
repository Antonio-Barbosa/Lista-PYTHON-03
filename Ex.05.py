n1 = int(input('n: '))
n2 = int(input('n: '))
while n1 % n2 != 0:
    n1, n2 = n2, n1 % n2
print (n2)

