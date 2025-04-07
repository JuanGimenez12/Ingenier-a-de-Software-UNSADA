# PROGRAMA PARA LA CALCULADORA BÁSICA
# Grupo 1 - IDS

def suma():                                                         # Función para la suma
    while True:                                                     # Bucle que se repite hasta que los datos ingresados sean válidos
        num1 = input("\nIngrese el primer número: ")                # Solicita primer número como string
        num2 = input("\nIngrese el segundo número: ")               # Solicita segundo número

        if not num1.isdigit() or not num2.isdigit():                # Verifica que ambos sean dígitos positivos
            print("\n⚠ Error: Debe ingresar solo números enteros positivos.")
            continue                                                # Vuelve al inicio del bucle

        num1, num2 = int(num1), int(num2)                           # Convierte ambos números a enteros

        if num1 <= 0 or num2 <= 0:                                  # Verifica que sean estrictamente positivos
            print("\n⚠ Error: Debe ingresar solo números enteros POSITIVOS.")
            continue

        resultado = num1 + num2                                     # Realiza la suma
        print(f"\nEl resultado de la suma es: {resultado}")         # Muestra el resultado
        break                                                       # Sale del bucle al tener datos válidos


def resta():                                                        # Función para la resta
    while True:
        num1 = input("\nIngrese el primer número: ")                # Solicita primer número
        num2 = input("\nIngrese el segundo número: ")               # Solicita segundo número

        try:
            num1 = float(num1)                                      # conviwerte al número a decimal
            num2 = float(num2)
        except ValueError:                                          # Si hay letras o símbolos inválidos, genera mensaje de error
            print("\n⚠ Error: Debe ingresar valores numéricos.")
            continue

        valor1 = max(num1, num2)                                    # Se asegura de restar el número mayor al menor
        valor2 = min(num1, num2)
        resultado = valor1 - valor2
        print(f"\nEl resultado de la resta es: {resultado}")
        break


def multiplicacion():                                               # Función para la multiplicación
    while True:
        num1 = input("\nIngrese el primer número: ")
        num2 = input("\nIngrese el segundo número: ")

        if not num1.isdigit() or not num2.isdigit():                # Verifica que sean estrictamente positivos
            print("\n⚠ Error: Debe ingresar solo números enteros positivos.")
            continue

        num1, num2 = int(num1), int(num2)

        if num1 < 0 or num2 < 0:                                    # Verifica que sean números mayor a cero
            print("\n⚠ Error: Debe ingresar solo números enteros POSITIVOS.")
            continue

        resultado = num1 * num2
        print(f"\nEl resultado de la multipicación es: {resultado}")
        break


def division():                                                     # Función para la división
    while True:
        num1 = input("\nIngrese el primer número: ")
        num2 = input("\nIngrese el segundo número: ")

        try:
            num1 = float(num1)                                      # convierte a número decimal
            num2 = float(num2)
        except ValueError:
            print("\n⚠ Error: Debe ingresar valores numéricos.")
            continue

        numerador = max(num1, num2)                                 # coloca El número más grande como numerador
        denominador = min(num1, num2)

        if denominador == 0:                                        # Si EL DENOMINADOR es cero, lanza error
            print("\n⚠ Error: No se puede dividir por cero.")
            continue

        resultado = numerador / denominador                         # Realiza la división
        print(f"\nEl resultado de la división es: {resultado}")
        break


# ---------- MENÚ PRINCIPAL ----------

def menu_principal():                                               # Función principal del menú
    while True:
                                                                    # Imprime el menú con las opciones
        print("\n      Calculadora BÁSICA -  Grupo 1 IDS     ")
        print("-------------------------------------------")
        print("\n[1] - SUMAR. ")
        print("\n[2] - RESTAR. ")
        print("\n[3] - MULTIPLICAR. ")
        print("\n[4] - DIVIDIR. ")
        print("\n[0] - SALIR DEL PROGRAMA ")
        opcion = input("\nSELECCIONAR UNA OPCIÓN [0 a 4] Y PRESIONAR ENTER: __  ")

        if not opcion.isdigit():                                    # Valida que la opción sea un número
            print("\n⚠ Error: Debe ingresar solo números entre 0 y 4.")
            continue

        if opcion == "1":
            while True:
                suma()
                print("\nS - Volver a Sumar")
                print("\nN - Volver al menú principal")
                sub_opcion = input("\nIngrese su opción: ").upper()

                if sub_opcion == "S":
                    continue                                         # Repite la suma
                elif sub_opcion == "N":
                    break                                            # Sale al menú principal
                else:
                    print("\nOpción inválida. Regresando al menú principal.")
                    break

        elif opcion == "2":
            while True:
                resta()
                print("\nS - Volver a Restar")
                print("\nN - Volver al  menú  principal")
                sub_opcion = input("\nIngrese su opción: ").upper()

                if sub_opcion == "S":
                    continue
                elif sub_opcion == "N":
                    break
                else:
                    print("\nOpción inválida. Regresando al menú principal.")
                    break

        elif opcion == "3":
            while True:
                multiplicacion()
                print("\nS - Volver a Multiplicar")
                print("\nN - Volver al  menú principal")
                sub_opcion = input("\nIngrese su opción: ").upper()

                if sub_opcion == "S":
                    continue
                elif sub_opcion == "N":
                    break
                else:
                    print("\nOpción inválida. Regresando al menú principal.")
                    break

        elif opcion == "4":
            while True:
                division()
                print("\nS -Volver a Dividir")
                print("\nN Volver al menú principal")
                sub_opcion = input("\nIngrese su opción: ").upper()

                if sub_opcion == "S":
                    continue
                elif sub_opcion == "N":
                    break
                else:
                    print("\nOpción inválida. Regresando al menú principal.")
                    break

        elif opcion == "0":                                         # Opción para salir del programa
            print("\nHasta luego!")                                 # Mensaje de despedida
            break                                                   # Finaliza el bucle principal

        else:                                                       # Si la opción no está entre 0 y 4
            print("\nOpción inválida. Por favor, inténtelo de nuevo.")


menu_principal()                                                    # Llama al menú principal para iniciar el programa
