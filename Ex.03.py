A = 80000
B = 200000
txa = 0.03
txb = 0.015
anos = 0
while A <= B:
    anos = anos + 1
    A = A + A * txa
    B = B + B * txb
print(f'{anos} anos')
