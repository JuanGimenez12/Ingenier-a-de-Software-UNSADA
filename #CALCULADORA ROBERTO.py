def suma():                                                      # Función para la suma           
    while True:                                                  # Ciclo para validar la entrada
        num1 = input("\nIngrese el primer número: ")             # Solicita el primer número
        num2 = input("\nIngrese el segundo número: ")            # Solicita el segundo número

        if not num1.isdigit() or not num2.isdigit():             # Verifica que sean numéricos
            print("\n⚠ Error: Debe ingresar solo números enteros positivos.")
            continue                                             # Repite la solicitud

        num1, num2 = int(num1), int(num2)                        # Convierte a enteros

        if num1 <= 0 or num2 <= 0:                                 # Verifica que sean positivos 
            print("\n⚠ Error: Debe ingresar solo números enteros POSITIVOS.")
            continue                                             # Repite la solicitud

        resultado = num1 + num2
        print(f"\nEl resultado de la suma es: {resultado}")
        break                                                    # Sale del bucle al obtener datos válidos


def resta():                                                     # Función para la resta
    num1 = float(input("Ingrese el primer número: "))            # Solicita el primer número
    num2 = float(input("Ingrese el segundo número: "))           # Solicita el segundo número
    valor1 = max(num1, num2)                                     # Asigna el número mayor a valor1
    valor2 = min(num1, num2)                                     # Asigna el número menor a valor2
    resultado = valor1 - valor2                                  # Realiza la resta 
    print(f"El resultado de la resta es: {resultado}")           # Muestra el resultado

def multiplicacion():                                            # Función para la multiplicación    
    num1 = float(input("Ingrese el primer número: "))            # Solicita el primer número
    num2 = float(input("Ingrese el segundo número: "))           # Solicita el segundo número
    resultado = num1 * num2                                      # Realiza la multiplicación
    print(f"El resultado de la multiplicación es: {resultado}")  # Muestra el resultado

def division():                                                  # Función para la división
    num1 = float(input("Ingrese el primer número: "))            # Solicita el primer número
    num2 = float(input("Ingrese el segundo número: "))           # Solicita el segundo número
    
    numerador = max(num1,num2)                                   #Asigna el valor más alto al numerador
    denominador = min(num1, num2)                                #Asigna el valor más bajo al denominador
    
    if denominador != 0:                                         # Verifica que el denominador no sea cero
        resultado = numerador / denominador                      # Realiza la división
        print(f"\nEl resultado de la división es: {resultado}")  # Muestra el resultado
    else:                                                        # Si el denominador es cero
        print("Error: No se puede dividir por cero")             # Muestra un mensaje de error

def menu_principal():                                            # Función para el menú principal
    while True:                                                  # Ciclo para mostrar el menú
        print("\n      Calculadora BÁSICA -  Grupo 1 EDD     ")  # Título del menú
        print("-------------------------------------------")
        print("\n[1] - SUMAR. ")
        print("\n[2] - RESTAR. ")
        print("\n[3] - MULTIPLICAR. ")
        print("\n[4] - DIVIDIR. ")
        print("\n[0] - SALIR DEL PROGRAMA ")
        opcion = input("\nSELECCIONAR UNA OPCIÓN [0 a 4] Y PRESIONAR ENTER: __  ") # Solicita la opción

        if not opcion.isdigit():                                  # Verifica si la entrada NO es numérica
            print("⚠ Error: Debe ingresar solo números entre 0 y 4.")  # Mensaje de error
            continue                                              # Vuelve a pedir la opción

        if opcion == "1":                                         # Si la opción es 1
            while True:

                suma()                                            # Llama a la función suma
                print("\nS - Volver a Sumar")
                print("\nN - Volver al menú principal")
                sub_opcion = input("\nIngrese su opción: ").upper()  # Convierte a mayúsculas

                if sub_opcion == "S":                             # Si la opción es S
                    continue                                      # Repite la suma
                elif sub_opcion == "N":                           # Si la opción es N
                    return menu_principal()                       # Vuelve al menú principal
                else:
                    print("Opción inválida. Regresando al menú principal.") # Mensaje de error
                    return menu_principal()                       # Vuelve al menú principal


        elif opcion == "2":                                       # Si la opción es 2
            resta()                                               # Llama a la función resta
            print("1. Volver a Restar")                           # Opción para volver a restar
            print("2. Volver al menú principal")
            sub_opcion = input("Ingrese su opción: ")             # Solicita la opción
            if sub_opcion == "1":                                 # Si la opción es 1
                resta()                                           # Repite la resta
            elif sub_opcion == "2":                               # Si la opción es 2
                return menu_principal()                           # Vuelve al menú principal
            else:
                print("Opción inválida. Regresando al menú principal.")  # Mensaje de error


        elif opcion == "3":                                      # Si la opción es 3
            multiplicacion()
            print("1. Volver a Multiplicar")                     # Opción para volver a multiplicar
            print("2. Volver al menú principal")                 # Opción para volver al menú principal
            sub_opcion = input("Ingrese su opción: ")            # Solicita la opción
            if sub_opcion == "1":                                # Si la opción es 1
                multiplicacion()                                 # Repite la multiplicación
            elif sub_opcion == "2":                              # Si la opción es 2
                return menu_principal()                          # Vuelve al menú principal
            else:
                print("Opción inválida. Regresando al menú principal.")  # Mensaje de error

                
        elif opcion == "4":                                      # Si la opción es 4 
            division()                                           # Llama a la función división
            print("1. Volver a Dividir")                         # Opción para volver a dividir
            print("2. Volver al menú principal")                 # Opción para volver al menú principal
            sub_opcion = input("Ingrese su opción: ")            # Solicita la opción
            if sub_opcion == "1":                                # Si la opción es 1
                division()                                       # Repite la división
            elif sub_opcion == "2":                              # Si la opción es 2
                return menu_principal()                          # Vuelve al menú principal
            else:
                print("Opción inválida. Regresando al menú principal.")   # Mensaje de error               

 
        elif opcion == "0":                                      # Si la opción es 0
            print("Hasta luego!")                                # Mensaje de despedida
            break                                                # Sale del bucle y termina el programa
        else:                                                    # Si la opción no es válida
            print("Opción inválida. Por favor, inténtelo de nuevo.")  # Mensaje de error

menu_principal()