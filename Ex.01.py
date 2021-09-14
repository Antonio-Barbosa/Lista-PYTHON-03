nota= float(input('Nota: '))
while nota < 0 or nota > 10 :
    nota = float(input('Nota inválida, digite novamente: '))
else :
    print(f'nota final {nota}: ')
