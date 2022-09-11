# Funcion de ingreso de patente

def ingreso_patente(patente_ingresada):
    patente_nueva = patente_ingresada
    print(patente_nueva)
    return patente_nueva

# Funcio para verificar que no sea un cliente existente.
def verificar(patente_nueva1):
    print('valor con el que llega',patente_nueva1)
    lista1 = []
    patente_registrada = str('JKI203')
    km = 1000
    fecha_ulti_serv = '10-08-2022'
    model = 'Peugot 206'
    año = 2010
    marca_aceite_filtro = 'Ejemplo'
    patente_nueva1 = str(patente_nueva1)
    print('tipopatentenueva',type(patente_nueva1))
    print('patente nueva',patente_nueva1)
    print('patente: ',patente_registrada)
    #lista1.append(patente_registrada, km, fecha_ulti_serv, model, año, marca_aceite_filtro)
    
    if patente_nueva1 == patente_registrada:
        print('Este auto tiene historial, el cual detallaremos a continuacion')
        print('-----------------------------------------------------------------------------------------------------------------------------------')
        
    else:
        print('Cliente nuevo')
        print('-----------------------------------------------------------------------------------------------------------------------------------')
        

# Main
print('Bienvenido')
print('-----------------------------------------------------------------------------------------------------------------------------------')
nuevo_ingreso = ingreso_patente(input('Ingresde la patente del vehiculo: '))
print('-----------------------------------------------------------------------------------------------------------------------------------')
verificar(nuevo_ingreso)
