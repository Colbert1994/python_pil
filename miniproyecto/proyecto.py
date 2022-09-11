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
def patente():
    """ Almacena la patente del auto

    Returns:
        string: recibe por teclado la patente del auto
    """
    patente = input('Ingrese patente del auto: ')
    return patente

def verificar_cliente(patente_cliente):
    """verifiar si la patente ingresada esta asociada a un cliente existente

    Args:
        patente_cliente (string): compara solo las patentes para saber si es cliente.
    """
    patente = 'JKI203'
    km = 1000
    fecha_ultimo_service = '12 agosto 2022'
    modelo = 'Peugot 208'
    año = 2010
    marca_aceite_filtro = 'Marca ejemplo'
    cliente_existente = {
        'patente': patente,
        'K.M': km,
        'Fecha de ultimo service': fecha_ultimo_service,
        'Modelo': modelo,
        'Año': año,
        'Marca de aceite y filtro utilizado': marca_aceite_filtro
    }
    if patente_cliente == cliente_existente[patente]: #revisar por que no hace lo que tiene que hacer
        print('Es un cliente existente')
    return cliente_existente

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
    nuevo_auto = []
    patente = input('Ingrese la patente del vehiculo: ')
    km = int(input('Ingrese el kilometraje del vehiculo: '))
    ultimo_service = input('Ingrese la ultima fecha de service en formato dd/mm/aa: ')
    modelo = input('Ingrese el modelo del auto y el año: ')
    servicio = input('Ingrese el servicio que se realizo: ')
    nuevo_auto.append(patente, km, ultimo_service, modelo, servicio)
    return nuevo_auto

def calcular_proximo_serv(nuevo_auto):
    """calcula el proximo service del auto ingresado

    Args:
        nuevo service: int
        nuevo_auto.km: int
        
    """
    nuevo_service = nuevo_auto.km + 15000
    return print('El proximo servicio es a los : ',nuevo_service,'km.') # no recuerdo si tenia que retornar o printear

def ingreso():
    print('Bienvenido: ')
    nuevo_ingreso = input('Ingrese la patente del auto: ')
    return nuevo_ingreso



# Programa main 

print('Bienvenido')
cliente = input('Ingrese la matricula del auto: ')
verificar_cliente(cliente)
if verificar_cliente == True:
    print('Cliente existente')
else:
    ingreso()
    nuevo_cliente()
    calcular_proximo_serv(nuevo_cliente)
    
