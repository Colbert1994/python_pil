# Bucles

# Bucle For Tengo que decirle la cantidad de veces
# Creamos una lista
lista = [True, False, 1, 2, 3, 4, 'Hola']
lista_1 = []
for i in lista:
    print(i)
for i in range(3):
    #Ingreso de datos
    dato_ingreso = input('Ingrese un número: ')
    #Validacion
    if dato_ingreso.isnumeric():
        
        lista_1.append(int(dato_ingreso)) # Agregamos en la lista vacia
    #mas corto: lista.append(int(input('Ingrese un numero: ')))
    else:
        print('No es un numero.')
        break # Corta el bucle.    
print(lista_1)


