# 9 Septiembre 2025 - 8AM  +0.1 primer corte
while True:
    entrada = input("Ingresa un numero (o escribe 'salir' para terminar): ")

    if entrada == "salir" or entrada == "SALIR" or entrada == "Salir":
        print("Hasta pronto.")
        break

#Solo para verificar que el caracter ingresado sea un numero.
    #es_numero = True
    #for n in entrada:
        if n < '0' or n > '9':
            es_numero = False
            break

    #if not es_numero:
        print("Por favor, ingresa un número válido.")
        continue

    numero = int(entrada)

    if numero < 2:
        print(str(numero) + " no es un número primo.")
        continue

    primo = True
    i = 2
    while i * i <= numero:
        if numero % i == 0:
            primo = False
            break
        i = i + 1

    if primo:
        print(str(numero) + " es un número primo.")
    else:
        print(str(numero) + " no es un número primo.")


