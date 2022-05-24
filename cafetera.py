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
cafe()