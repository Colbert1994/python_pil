# programa: que lea 4 palabras(ingresadas por el usuario)
# calcule la longitud de cada una de ellas y las despliegue con su
# longitud indicada con asteriscos.
# ej: Arbol *****
# tiene que mostrar la palabra ingresada y la cantidad de caracteres
# Uno -> ***

# Ingreso de palabras.
palabra_1 = input('Ingrese una palabra: ')
palabra_2 = input('Ingrese una palabra: ')
palabra_3 = input('Ingrese una palabra: ')
palabra_4 = input('Ingrese una palabra: ')

# Calcular la longitud de cada palabra
long_palabra1 = len(palabra_1)
long_palabra2 = len(palabra_2)
long_palabra3 = len(palabra_3)
long_palabra4 = len(palabra_4)

# Transformar la longitud con asteriscos
ast_1 = '*' * long_palabra1 #ast1 = '*' * len(palabra1)
ast_2 = '*' * long_palabra2 #ast2 = '*' * len(palabra2)
ast_3 = '*' * long_palabra3 #ast3 = '*' * len(palabra3)
ast_4 = '*' * long_palabra4 #ast4 = '*' * len(palabra4)

# Mostrar palabra, longitud en asteriscos 
# print(len(palabra_1 * '*'))
print(palabra_1, ast_1)
print(palabra_2, ast_2)
print(palabra_3, ast_3)
print(palabra_4, ast_4)

# Hacer un diccionario
diccionario_1 = {
    palabra_1:ast_1,
    palabra_2:ast_2,
    palabra_3:ast_3,
    palabra_4:ast_4
}

print(diccionario_1)