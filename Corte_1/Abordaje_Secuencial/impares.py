# 9 Septiembre 2025 - 8AM  +0.1 primer corte
while True:
    i = input("Ingresa un numero (o escribe 'salir' para terminar): ")

    if i.lower() == 'salir':
        print("Hasta pronto.")
        break

    try:
        num = int(i)
        if num % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")
    except ValueError:
        print("Ingresa un número o 'salir' para terminar.")



