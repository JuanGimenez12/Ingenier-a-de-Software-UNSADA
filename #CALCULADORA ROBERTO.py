# PROGRAMA PARA LA CALCULADORA BÁSICA
# Grupo 1 - IDS

def suma():
    while True:
        num1 = input("\nIngrese el primer número: ")
        num2 = input("\nIngrese el segundo número: ")

        if not num1.isdigit() or not num2.isdigit():
            print("\n⚠ Error: Debe ingresar solo números enteros positivos.")
            continue

        num1, num2 = int(num1), int(num2)

        if num1 <= 0 or num2 <= 0:
            print("\n⚠ Error: Debe ingresar solo números enteros POSITIVOS.")
            continue

        resultado = num1 + num2
        print(f"\nEl resultado de la suma es: {resultado}")
        break


def resta():
    num1 = float(input("\nIngrese el primer número: "))
    num2 = float(input("\nIngrese el segundo número: "))
    valor1 = max(num1, num2)
    valor2 = min(num1, num2)
    resultado = valor1 - valor2
    print(f"\nEl resultado de la resta es: {resultado}")


def multiplicacion():
    while True:
        num1 = input("\nIngrese el primer número: ")
        num2 = input("\nIngrese el segundo número: ")

        if not num1.isdigit() or not num2.isdigit():
            print("\n⚠ Error: Debe ingresar solo números enteros positivos.")
            continue

        num1, num2 = int(num1), int(num2)

        if num1 < 0 or num2 < 0:
            print("\n⚠ Error: Debe ingresar solo números enteros POSITIVOS.")
            continue

        resultado = num1 * num2
        print(f"\nEl resultado de la multiplicación es: {resultado}")
        break


def division():
    num1 = float(input("\nIngrese el primer número: "))
    num2 = float(input("\nIngrese el segundo número: "))

    numerador = max(num1, num2)
    denominador = min(num1, num2)

    if denominador != 0:
        resultado = numerador / denominador
        print(f"\nEl resultado de la división es: {resultado}")
    else:
        print("\nError: No se puede dividir por cero")


def menu_principal():
    while True:
        print("\n      Calculadora BÁSICA -  Grupo 1 IDS     ")
        print("-------------------------------------------")
        print("\n[1] - SUMAR.")
        print("\n[2] - RESTAR.")
        print("\n[3] - MULTIPLICAR.")
        print("\n[4] - DIVIDIR.")
        print("\n[0] - SALIR DEL PROGRAMA")
        opcion = input("\nSELECCIONAR UNA OPCIÓN [0 a 4] Y PRESIONAR ENTER: __  ")

        if not opcion.isdigit():
            print("\n⚠ Error: Debe ingresar solo números entre 0 y 4.")
            continue

        if opcion == "1":
            while True:
                suma()
                print("\nS - Volver a Sumar")
                print("\nN - Volver al menú principal")
                sub_opcion = input("\nIngrese su opción: ").upper()
                if sub_opcion == "S":
                    continue
                elif sub_opcion == "N":
                    break
                else:
                    print("\nOpción inválida. Regresando al menú principal.")
                    break

        elif opcion == "2":
            while True:
                resta()
                print("\nS - Volver a Restar")
                print("\nN - Volver al menú principal")
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
                print("\nN - Volver al menú principal")
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
                print("\nS - Volver a Dividir")
                print("\nN - Volver al menú principal")
                sub_opcion = input("\nIngrese su opción: ").upper()
                if sub_opcion == "S":
                    continue
                elif sub_opcion == "N":
                    break
                else:
                    print("\nOpción inválida. Regresando al menú principal.")
                    break

        elif opcion == "0":
            print("\nHasta luego!")
            break

        else:
            print("\nOpción inválida. Por favor, inténtelo de nuevo.")


# Llamada al programa principal
menu_principal()
