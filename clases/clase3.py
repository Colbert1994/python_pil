# Condicionales en python

# Generamos una variable y asignamos un valor
a = 3
b = 2
c = 5
resultado = a + b # Sumamos variables
print(resultado) # Mostramos el resultado de la suma

# Condicional if

# Preguntamos si A es mayor que B
if a > b: # Devuelve un booleano(True or False)
    print('A es mayor que B')
    if a > c:
        print('A es mayor que C')
    else:
        print('C es mayor a A y a B')

# Ejemplos de condicionales
else:
    print('El mayor es B')
    
if a == 3:
    print('A es igual a 3')

if a == '3':
    print('A es igual a 3 ')
else:
    print('A no es igual')
    
if a != 3:
    print('A no es igual a 3')
else:
    print('A es igual a 3 ')

