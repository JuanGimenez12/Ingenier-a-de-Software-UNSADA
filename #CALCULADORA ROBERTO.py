#PROGRAMA PARA LA CALCULADORA BÁSICA
# Grupo 1 - IDS
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
    num1 = float(input("\nIngrese el primer número: "))            # Solicita el primer número
    num2 = float(input("\nIngrese el segundo número: "))           # Solicita el segundo número
    valor1 = max(num1, num2)                                     # Asigna el número mayor a valor1
    valor2 = min(num1, num2)                                     # Asigna el número menor a valor2
    resultado = valor1 - valor2                                  # Realiza la resta 
    print(f"\nEl resultado de la resta es: {resultado}")           # Muestra el resultado

def multiplicacion():                                            # Función para la multiplicación
    while True:                                                  # Ciclo para validar la entrada
        num1 = input("\nIngrese el primer número: ")             # Solicita el primer número
        num2 = input("\nIngrese el segundo número: ")            # Solicita el segundo número

        if not num1.isdigit() or not num2.isdigit():                            # Verifica que sean numéricos
            print("\n⚠ Error: Debe ingresar solo números enteros positivos.")
            continue                                                             # Repite la solicitud

        num1, num2 = int(num1), int(num2)                                        # Convierte a enteros

        if num1 < 0 or num2 < 0:                                                 # Verifica que sean positivos
            print("\n⚠ Error: Debe ingresar solo números enteros POSITIVOS.")
            continue                                                             # Repite la solicitud

        resultado = num1 * num2
        print(f"\nEl resultado de la multipicación es: {resultado}")
        break                                                                    # Sale del bucle al obtener datos válidos

def division():                                                  # Función para la división
    num1 = float(input("\nIngrese el primer número: "))            # Solicita el primer número
    num2 = float(input("\nIngrese el segundo número: "))           # Solicita el segundo número
    
    numerador = max(num1,num2)                                   #Asigna el valor más alto al numerador
    denominador = min(num1, num2)                                #Asigna el valor más bajo al denominador
    
    if denominador != 0:                                         # Verifica que el denominador no sea cero
        resultado = numerador / denominador                      # Realiza la división
        print(f"\nEl resultado de la división es: {resultado}")  # Muestra el resultado
    else:                                                        # Si el denominador es cero
        print("\nError: No se puede dividir por cero")             # Muestra un mensaje de error

def menu_principal():                                            # Función para el menú principal
    while True:                                                  # Ciclo para mostrar el menú
        print("\n      Calculadora BÁSICA -  Grupo 1 IDS     ")  # Título del menú
        print("-------------------------------------------")
        print("\n[1] - SUMAR. ")
        print("\n[2] - RESTAR. ")
        print("\n[3] - MULTIPLICAR. ")
        print("\n[4] - DIVIDIR. ")
        print("\n[0] - SALIR DEL PROGRAMA ")
        opcion = input("\nSELECCIONAR UNA OPCIÓN [0 a 4] Y PRESIONAR ENTER: __  ") # Solicita la opción

        if not opcion.isdigit():                                  # Verifica si la entrada NO es numérica
            print("\n⚠ Error: Debe ingresar solo números entre 0 y 4.")  # Mensaje de error
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
                    print("\nOpción inválida. Regresando al menú principal.") # Mensaje de error
                    return menu_principal()                       # Vuelve al menú principal


        elif opcion == "2":                                        # Si la opción es 2
            while True:

            resta()                                               # Llama a la función resta
            print("\nS - Volver a Restar")                           # Opción para volver a restar
            print("\nN - Volver al  menú  principal")
            sub_opcion = input("\nIngrese su opción: ").upper()      # Convierte a mayúsculas #  Solicita la opción
                
            if sub_opcion == "S":                                 # Si la opción es S
                continue                                           # Repite la resta
            elif sub_opcion == "N":                               # Si la opción es N
                return menu_principal()                           # Vuelve al menú principal
            else:
                print("\nOpción inválida. Regresando al menú principal.")  # Mensaje de error
                return menu_principal()

        elif opcion == "3":                                      # Si la opción es 3
            while True:
        
            multiplicacion()                                    # Llama a la función multiplicación
            print("\nS - Volver a Multiplicar")                     # Opción para volver a multiplicar
            print("\nN - Volver al  menú principal")                 # Opción para volver al menú principal
            sub_opcion = input("\nIngrese su opción: ").upper()      # Convierte a mayúsculas #  Solicita la opción
            if sub_opcion == "S":                                # Si la opción es S
                continue                               # Repite la multiplicación
            elif sub_opcion == "N":                              # Si la opción es N
                return menu_principal()                          # Vuelve al menú principal
            else:
                print("\nOpción inválida. Regresando al menú principal.")  # Mensaje de error
                return menu_principal()
                
        elif opcion == "4":                                      # Si la opción es 4 
            while True:
                
            division()                                           # Llama a la función división
            print("\nS -Volver a Dividir")                         # Opción para volver a dividir
            print("\nN Volver al menú principal")                 # Opción para volver al menú principal
            sub_opcion = input("\nIngrese su opción: ").upper()      # Convierte a mayúsculas        # Solicita la opción
            if sub_opcion == "S":                                # Si la opción es 1
               continue                                       # Repite la división
            elif sub_opcion == "N":                              # Si la opción es 2
                return menu_principal()                          # Vuelve al menú principal
            else:
                print("\nOpción inválida. Regresando al menú principal.")   # Mensaje de error               
                return menu_principal()
 
        elif opcion == "0":                                      # Si la opción es 0
            print("\nHasta luego!")                                # Mensaje de despedida
            break                                                # Sale del bucle y termina el programa
        else:                                                    # Si la opción no es válida
            print("\nOpción inválida. Por favor, inténtelo de nuevo.")  # Mensaje de error

menu_principal()
