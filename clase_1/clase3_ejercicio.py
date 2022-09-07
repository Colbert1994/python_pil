# Realizar un menu de un cajero automatico
# deposito 
# extraccion
# transferencia
# salir
# solo se detendra la opcion salir en el menu principal

# definimos menu


print('Bienvenido')
selec = 0
while selec != 4:
    selec = int(input('Ingrese 1 para Depositos.''\n''Ingrese 2 para Extracciones.''\n''Ingrese 3 para Transferencia.''\n''Ingrese 4 para Salir.''\n'':'))

    if selec == 1:
        print('Usted esta en Deposito')
        deposito = int(input('Ingrese la cantidad a depositar: '))
        
    elif selec == 2:
        print('Usted esta en extracciones')
        extraccion = int(input('Ingrese el monto a extraer: '))
        
    elif selec == 3:
        print('Usted esta en transferencia')
        transferencia: int(input('Ingrese el monto a transferir: '))
    else:
        print('Adios')