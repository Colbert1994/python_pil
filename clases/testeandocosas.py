def suma_dos(x, y):
    suma = x + y
    resta = x - y
    valor_x = x
    valor_y = y
    diccionar1 = {
        'Suma': suma,
        'Resta': resta,
        'Primer valor': valor_x,
        'Segundo valor': valor_y
    }
    return diccionar1['Suma']
def mayor(x, y):
    if x > y:
        may = x
        print('El primer valor es mayor ',x )
    else:
        may = y
        print(' El segundo valor es mayor ',y)
    return may

# programa main
a = int(input('Ingrese un numero: '))
b = int(input('Ingrese otro numero: '))
resultado = suma_dos(a, b)
print('el resultado de la suma es: ',resultado)
c = mayor(resultado, b)
print('otra vez')
z = suma_dos(resultado, c)
print(z)
if c > z:
    print('asd')
else:
    print('dsa')
