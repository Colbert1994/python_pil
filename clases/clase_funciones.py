# Funcion base
# Elementos:
# Nombre
# Argumentos
# Codigo
# Retorno

# Creamos nuestra primera funcion

# Aca tenemos nombre, y argumento()
def sumar(a, b):
    
    # Codigo
    resultado = a + b
    
    # Retorno
    return resultado

# Invocamos la funcion
resultado_suma = sumar(2,3)

# Mostramos el resultado
print(resultado_suma) #otra forma seria print(sumar(2,3))


# Funcion 2 (funcion sin parametros)

# Definimos
def resta():
    # Codigo
    resultado = 2 - 3
    
    # Retorno
    return resultado

# Mostramos funcion resta
print(resta())

# Funcion 3 (funcion haga la operacion sin devolver nada)

# definimos

def saludo(x): #solo pedimos la cantidad de veces que queremos que se repita porque el nombre lo pedimos abajo.
    """Esta funcion recoge los nombres ingresados por el
    usuario y devuelve los mismos en formato lista"""
    
    # Creamos la lista para que no se pierda la lista de nombres
    lista_nombres = []
    
    # Codigo
    for i in range(x):
        nombre = input('Ingrese su nombre: ')
        print('Hola', nombre)
        
        # Guardamos el nombre 
        lista_nombres.append(nombre)
    
    # Mostramos la lista de nombres guardados
    print(lista_nombres)
    
    # No tenemos retorno en esta funcion / edit: nuestro programa necesita sacar la lista y utilizarla afuera
    return lista_nombres

# Funcion para ordenar nombres tome los nombres de la otra funcion
# y los ordene alfabeticamente(ordena strings)

# definimos
def orden(lista, sentido):
    """_summary_ Esta funcion nos permite ordenar listas en base a un sentido determinado

    Args:
        lista (list): lista generica
        sentido (bool): Definir si la lista se ordena de mayor a menor o de menor a mayor

    Returns:
        list: lista ordenada
    """
    
    # Codigo
    # tomamos a la lista y la ordenamos
    lista.sort(reverse= sentido)
    
    #retornamos la lista
    return lista

    


# Invocamos la funcion y pedimos la cantidad de veces 

nombres = saludo(int(input('Ingrese la cantidad de saludos: '))) # Esto es una lista, porque cuando termine
# de correr la funcion devolvera la lista de todos los nombres que itero.

# Invocamos lista 
print(
    orden(nombres, True)
)
#orden(nombres, True)

# definimos otra funcion parametros posicional
def prueba(a, b, c):
    # Codigo
    print(a, b, c)
# 1er orden
#prueba(1, 2, 3)
# 2do orden
#a = 3
#b = 2
#c = 1
#prueba(b, a, c)
#prueba(a=a, b=b, c=c)
#prueba(b=b, c=c, a=a) # igualamos el argumento con la variable

