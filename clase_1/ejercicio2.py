# Idear un programa que solicité al usuario dos números enteros y el programa deberá retornar aquellos
# números pares que esten dentro del rango formado entre los números ingresados.

# Ingreso de números
a = int(input('Ingrese el primer número: '))
b = int(input('Ingrese el segundo número: '))
# Lista que acumulara los numeros
lista1 = []

# Ciclo for para guardar los numeros pares dentro del rango
for i in range(a, b-1):
    # Operacion para averiguar si es par
    par = i % 2
    # Comparacion para agregar
    if par == 0:
        #Agregamos a la lista
        lista1.append(i)
# Mostramos en pantalla la lista
print(lista1)

    