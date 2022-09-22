# Realizar un menu de un cajero automatico donde el usuario pueda escoger entre las siguientes opciones
# Deposito-Extraccion-Transferencia-Salir
# En todos los casos se debe pedir al usuario un monto de dinero y el programa debera mostrar en todo momento
# la seccion menu en la que se encuentra, pudiendo retomar al menu principal siempre que se quiera y solo se detendra
# cuando se ingrese la opcion salir en el menu principal.

menu = 'Operaciones: \n1. Deposito \n2. Extracciones \n3. Transferencia \n4. Salir'


# variable para inicializar el ciclo while
opc = 0
# Mensaje de Bienvenida
print('Bienvenido')
# Menu
print(menu)

# Ciclo While
while opc != 4:
    # Menu de cajero automatico
    opc = int(input('Ingrese la operación que desea realizar:'))
    
    # Condicion para opcion 1 Deposito
    if opc == 1:
        # Mensaje para saber donde se encuentra
        print('Usted esta en Despositos')
        # Variable de monto a depositar
        monto = int(input('Ingrese el monto a depositar: '))
        # Variable para retornar al menu principal
        retornar = input('Desea realizar otra operación? Y/N: ')
        if retornar == 'Y':
            print(menu)
            
        else:
            print('Saliendo del sistema...\nAdios.')
            break
    
    # Condicion para opcion 2 Extraccion
    elif opc == 2:
        # Mensaje para saber donde se encuentra
        print('Usted esta en Extracciones')
        # Variable para el monto a extraer
        monto = int(input('Ingrese el monto de extracción: '))
        # Variable para retornar
        retornar = input('Desea realizar otra operación? Y/N: ')
        if retornar == 'Y':
            print(menu)
        else:
            print('Saliendo del Sistema... \nAdios.')
            break     
    
    # Condicion para opccion 3 Transferencia
    elif opc == 3:   
        # Mensaje para saber donde se encuentra
        print('Usted esta en Transferencias')
        # Variable para el monto a transferir
        monto = int(input('Ingrese el monto a transferir: '))
        # Variable para retornar
        retornar = input('Desea realiar otra operación? Y/N: ')
        if retornar == 'Y':
            print(menu)
        else:
            print('Saliendo del Sistema... \nAdios.')
            break
    
    # Opcion Salir
    elif opc == 4:
        print('Saliendo del Sistema... \nAdios.')
    else:
        print('Opcion incorrecta, por favor ingrese una opccion valida...')
        print(menu)
        
        