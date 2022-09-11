# Funcion de ingreso de patente

def ingreso_patente(patente_ingresada):
    patente_nueva = patente_ingresada
    print(patente_nueva)
    return patente_nueva

# Funcion nuevo cliente
def nuevo_cliente():
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

# Funcio para verificar que no sea un cliente existente.
def verificar(patente_nueva1):
    cliente_existente = {
        'Patente_registrada': 'JKI203',
        'K.M': 1000,
        'Fecha de ultimo service': '10-08-2022',
        'Modelo': 'Peugot 206',
        'Año': 2010,
        'Marca de aceite y filtro utilizado': 'Marca Ejemplo'
    }
    patente_existente = cliente_existente['Patente_registrada']
    if patente_existente == patente_existente:
        print('Es un cliente existente')
        print('A continuaciçon le detallamos un resumen')
        print(cliente_existente)
    else: 
        print('Cliente nuevo.')
        nuevo_cliente()
    return cliente_existente

# Main
print('Bienvenido')
print('-----------------------------------------------------------------------------------------------------------------------------------')
nuevo_ingreso = ingreso_patente(input('Ingresde la patente del vehiculo: '))
print('-----------------------------------------------------------------------------------------------------------------------------------')
verificar(nuevo_ingreso)
