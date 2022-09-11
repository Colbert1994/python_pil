# un sistema de registro para talleres mecanicos, un formulario, donde 
# cargas los autos, otro punto donde le cargas la historia clinica por decirte
# y con la fecha y kms registrados, calculas cuando tienen que hacer un service de nuevo

# Programa.
# Ingrese de patente de auto.
# si es cliente, mostrar historial de servicio ( se puede iterar)
# si no es cliente, pedir datos(año del vehiculo, modelo), y que servicio se va a realizar.
# ingresemos la fecha en el dia que realizamos el servicio
# fecha del ultimo servicio.
# kilometraje 
# calcular el proximo servicio
# nuestro programa tiene que que decirle cuando tiene que volver por la cantidad de kilometraje ( buscar la cantidad de años para hacer el service)
# cuando hacer cambio de aceite y filtro cada 15k km.

# Funciones necesarias
def patente_ingresada(nueva_patente):
    """ Almacena la patente del auto

    Returns:
        string: recibe por teclado la patente del auto
    """
    patente_nuevo_cliente = nueva_patente
    return patente_nuevo_cliente

def verificar_cliente(patente_nuevo_cliente):
    """verifiar si la patente ingresada esta asociada a un cliente existente

    Args:
        patente_cliente (string): compara solo las patentes para saber si es cliente.
    """
    cliente_existente = {
        'Patente_registrada': 'JKI203',
        'K.M': 1000,
        'Fecha de ultimo service': '10-08-2022',
        'Modelo': 'Peugot 206',
        'Año': 2010,
        'Marca de aceite y filtro utilizado': 'Marca Ejemplo'
    }
    patente_existente = cliente_existente['Patente_registrada']
    if patente_nuevo_cliente == patente_existente:
        print('Es un cliente existente')
        print('A continuaciçon le detallamos un resumen')
        print(cliente_existente)
        
    else: 
        print('Cliente nuevo.')
        nuevo_cliente()
    return cliente_existente, 

def nuevo_cliente():
    """nuevo cliente: toma los datos del nuevo cliente

    Returns:
        patente: string
        km: int
        ultimo_service: string
        modelo: string
        servicio: string
        nuevo_auto: list
    """
    nuevo_auto = {}
    patente = input('Ingrese la patente del vehiculo: ')
    km = int(input('Ingrese el kilometraje del vehiculo: '))
    ultimo_service = input('Ingrese la ultima fecha de service en formato dd/mm/aa: ')
    modelo = input('Ingrese el modelo del auto y el año: ')
    servicio = input('Ingrese el servicio que se realizo: ')
    nuevo_auto = {
        'Patente:': patente,
        'Km: ': km,
        'Fecha de ultimo service: ':ultimo_service,
        'Modelo: ': modelo,
        'Marca de aceite y filtro utilzado: ': servicio
    }
    return nuevo_auto

def calcular_proximo_serv(nuevo_auto):
    """calcula el proximo service del auto ingresado

    Args:
        nuevo service: int
        nuevo_auto.km: int
        
    """
    nuevo_service = nuevo_auto.km + 15000
    print('El proximo servicio es a los : ',nuevo_service,'km.') # no recuerdo si tenia que retornar o printear

def ingreso():
    print('Bienvenido: ')
    nuevo_ingreso = input('Ingrese la patente del auto: ')
    return nuevo_ingreso



# Programa main 

print('Bienvenido')
nuevo_ingres = patente_ingresada(input('Ingrese la patente del auto: '))
verificar_cliente(nuevo_ingres)



        
    




