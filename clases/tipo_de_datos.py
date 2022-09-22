# Tipos de datos
# strings (STR)
a = 'Esto Es Una Cadena'
b = "eso es otra cadena"

print(a, type(a))
print(b, type(b))

c = str(120.56)
print(c, type(c))
print(len(a))
print(a[0:4])
print(a[-1])

# Metodos de los strings

print(a.lower())
print(b.upper())
print(a.split())

# Listas
lista_1 = ['hola', 4, 2.5, True, [1,2,3,4], ('a', 'b')]
print(lista_1)
print(type(lista_1))
print(len(lista_1))
print(lista_1[2])
var_uno = lista_1[3]
print(var_uno)
print(type(var_uno))

# Metodos
lista_1.append('lista')
print(lista_1)
print(lista_1.index(('a', 'b')))
lista_1.insert(1, 5)
print(lista_1)

# Diccionario
usuario = {
    'nombre': 'Octavio',
    'apellido': 'Gomez',
    'edad': 38,
    'hobbies': ['Futbol', 'Musica'],
    'mascotas': False
    
}
print(usuario)
print(usuario['edad'])
print(len(usuario))

# Metodo de diccionario
print(usuario.get('puesto', 'No encontrado'))
keys_usuario = list(usuario.keys())
print(type(keys_usuario))
print(usuario.get(keys_usuario[0]))

print(usuario.values())
