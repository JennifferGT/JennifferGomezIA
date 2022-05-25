#Muestra un menú detallando los lugares de la cafetera.
def cafe():
    print("Seleccione el lugar de la cafetera: ")
    print("1. Cocina")
    print("2. Oficina")
    print("3. Restaurante")
    #Inicializamos en 0 el número de movimentos que realiza la cafetera.
    aumento = 0;
    #Ingresar por medio de número el lugar de la cafetera que desea encender.
    opcionMe = input("Insertar el lugar de la cafetera: ")
    #Crea una función que verifica el lugar de la cafetera
    # Si la cafetera está en la cocina se debe ingresar el número 1.
    if opcionMe == '1':
        #Imprime el menú de estado del café si está apagado se ingresa 0 y si está encendido se ingresa 1
        print("Seleccione el estado de la cafetera: ")
        print("0. Apagado")
        print("1. Encendido")
        #Ingresar el estado de la cafetera por medio de los números indicados
        opcionEstado = input("Inserte el estado de la cafetera: ")
        #Ingresar el número de la temperatura del agua de la cafetera.
        temperatura = int(input("Ingrese la temperatura de la cafetera: "))
        #Crea una función que verifica el estado de la cafetera.
        # Si la cafetera está apagado automaticamente se enciende y aumenta un movimiento de la maquita
        if opcionEstado == '0':
            opcionEstado = '1'
            aumento += 1
            #Verifica que la temperatura sea mayor que 90, para que la cafetera se apague 
            if temperatura >= 90:
                opcionEstado = '0'
                #Muestra un mensaje diciendo que el café está listo
                print("El café está listo ")
                print("El número de movimientos es:" + str(aumento))
            #Si la temperatura es menor que 90 se mantiene encendido 
            elif temperatura < 90:
                opcionEstado = '1'
                 #Muestra un mensaje diciendo que el café está listo
                print("El café aún no está listo ")
            else:
                print("Ingrese la temperatura del agua:")
         # Si la cafetera está encendida aumenta un movimiento de la maquita  verificando su temperatura  
        elif opcionEstado == '1':
            aumento += 1
            if temperatura >= 90:
                opcionEstado = '0'
                print("El café está listo ")
            elif temperatura < 90:
                opcionEstado = '1'
                print("El café aún no está listo ")
            else:
                print("Ingrese la temperatura del agua:")
        else:
         print("Ingrese el estado")
    # Si la cafetera está en la oficina se debe ingresar el número 2.
    elif opcionMe == '2':
        #Imprime el menú de estado del café si está apagado se ingresa 0 y si está encendido se ingresa 1
        print("Seleccione el estado de la cafetera: ")
        print("0. Apagado")
        print("1. Encendido")
        #Ingresar el estado de la cafetera por medio de los números indicados
        opcionEstado = input("Inserte el estado de la cafetera: ")
        #Ingresar el número de la temperatura del agua de la cafetera.
        temperatura = int(input("Ingrese la temperatura de la cafetera: "))
         # Si la cafetera está apagado automaticamente se enciende y aumenta un movimiento de la maquita
        if opcionEstado == '0':
            opcionEstado = '1'
            aumento += 1
            #Verifica que la temperatura sea mayor que 90, para que la cafetera se apague 
            if temperatura >= 90:
                opcionEstado = '0'
                #Muestra un mensaje diciendo que el café está listo
                print("El café está listo ")
                #Si la temperatura es menor que 90 se mantiene encendido
            elif temperatura < 90:
                opcionEstado = '1'
                #Muestra un mensaje diciendo que el café está listo
                print("El café aun no está listo ")
            else:
                print("Ingrese la temperatura del agua:")
        elif opcionEstado == '1':
            aumento += 1
            if temperatura >= 90:
                opcionEstado = '0'
                print("El café está listo ")
            elif temperatura < 90:
                opcionEstado = '1'
                print("El café aún no está listo ")
                #Si no cumple con las funciones imprime un mensaje de volver a ingresar la temperatura
            else:
                print("Ingrese la temperatura del agua:")
            #Si no cumple con las funciones, caso contrario imprime un mensaje
        else:
         print("Ingrese el estado")
     # Si la cafetera está en la restaurante se debe ingresar el número 3.
    elif  opcionMe == '3':
        #Imprime el menú de estado del café si está apagado se ingresa 0 y si está encendido se ingresa 1
        print("Seleccione el estado de la cafetera: ")
        print("0. Apagado")
        print("1. Encendido")
        #Ingresar el estado de la cafetera por medio de los números indicados
        opcionEstado = input("Inserte el estado de la cafetera: ")
        #Ingresar el número de la temperatura del agua de la cafetera.
        temperatura = int(input("Ingrese la temperatura de la cafetera: "))
         # Si la cafetera está apagado automaticamente se enciende y aumenta un movimiento de la maquita
        if opcionEstado == '0':
            opcionEstado = '1'
            aumento += 1
            #Verifica que la temperatura sea mayor que 90, para que la cafetera se apague 
            if temperatura >= 90:
                opcionEstado = '0'
                print("El café está listo ")
                #Si la temperatura es menor que 90 se mantiene encendido
            elif temperatura < 90:
                opcionEstado = '1'
                #Muestra un mensaje diciendo que el café está listo
                print("El café aún no está listo ")
                #Si no cumple con las funciones, caso contrario imprime un mensaje
            else:
                print("Ingrese la temperatura del agua:")
        elif opcionEstado == '1':
            aumento += 1
            if temperatura >= 90:
                opcionEstado = '0'
                print("El café está listo ")
            elif temperatura < 90:
                opcionEstado = '1'
                print("El café aún no está listo ")
                #Si no cumple con las funciones, caso contrario imprime un mensaje
            else:
                print("Ingrese la temperatura del agua:")
            #Si no cumple con las funciones, caso contrario imprime un mensaje
        else:
         print("Ingrese el estado")
        #Si no cumple con las funciones, caso contrario imprime un mensaje
    else:
        print("Ingrese el lugar")
    #Cierra la función café
cafe()