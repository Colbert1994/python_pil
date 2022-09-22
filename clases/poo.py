# Paradigma orientada a objetos.

# Clase padre

class Animal:
    def __init__(self, especie, edad):
        # Declarar los atributos
        self.especie = especie
        self.edad = edad
    # Metodos
    def hablar(self, sonido):
        print(sonido)
        

# Creamos nuestra primera clase
class Perro(Animal):
    
    # Atributos de clase == variables globales de la clase
    #especie = 'Mamiferos'
    
    # inicializar
    def __init__(self, nombre, raza, especie, edad):
        # Atributo tenemos que empezar con la palabra self
        # Atributo de instancia == variables locales.
        self.nombre = nombre
        self.raza = raza
        super().__init__(especie, edad)
    
    # Metodos
    
    # def jugar(self, objeto):
        #print('El perro esta jugando con', objeto)
    # def saludar(self):
    #    print('Guau, mi nombre es ', self.nombre)
    def saludar(self):
        print(f'{self.nombre} dio la pata')
           
           
class Gato(Animal):
    def __init__(self, nombre, raza,especie, edad):
        self.nombre = nombre
        self.raza = raza
        
        super().__init__(especie, edad)
    def saludar(self):
        print(f'{self.nombre} ronronea')


perro_1 = Perro('Firulais', 'Salchicha', 'Perro', 5)
#perro_2 = Perro('Ana', 'Collie')

print(f'Perro_1 -> {perro_1.nombre}, {perro_1.raza}, {perro_1.especie}, {perro_1.edad}')
perro_1.saludar()
#perro_1.ladrar()
#perro_1.jugar('Pelota')
#perro_1.saludar()
#print(f'Perro_2 -> {perro_2.nombre}, {perro_2.raza}, {perro_2.especie}')
#perro_2.saludar()
gato_1 = Gato('Tito', 'Calico', 'Felino', 3)
print(f'gato_1 -> {gato_1.nombre}, {gato_1.raza}, {gato_1.especie}, {gato_1.edad}')
gato_1.saludar()