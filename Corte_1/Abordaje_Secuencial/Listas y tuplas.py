##########Listas##########
##########################

my_Lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
#input()
print(my_Lista)
print(type(my_Lista)) #Imprime el tipo de objeto (en este caso, lista).
print(my_Lista[2])  #Imprime el elemento 2 (tener en cuenta que inicia en 0, por lo que el elemento 2 es "Amarillo").


print("my_lista size: ", len(my_Lista))  #Imprime el tamaño de la lista.
print(my_Lista[0:2]) #Imprime los elementos del número 0 al número 2.
print(my_Lista[:2])  #Imprime desde el primer elemento al número 2.


my_Lista.append('Blanco')  #Agrega elemento al final de la lista.
print(my_Lista)


my_Lista.insert(3, 'Negro')  #Inserta un elemento en un sitio específico, en este caso en el sitio 3, y el elemento "Negro".
print(my_Lista)


my_Lista.extend(['Marron', 'Gris'])  #Extiende/agrega elementos al final de la lista.
print(my_Lista)


print(my_Lista.index('Azul'))  #Imprime el número de posición en la que se encuentra un elemento, el Azul se encuentra en la posición 1.


#my_lista.remove('Magenta')
my_Lista.remove('Marron') #Elimina un elemento.
print(my_Lista)


my_Lista.insert(8, 'Marron')
print(my_Lista)


print(my_Lista.pop())  #Elimina y retorna el último elemento de la lista.
size=len(my_Lista)
print("Size= ", size)
#print)(my_Lista.pop(size))


my_Lista_3 = my_Lista*3  #Repite el número de veces indicado la lista.
print("my_Lista_3: ", my_Lista_3)


print("Sort:")

my_ListaSort = my_Lista.sort()  #Filtra los elementos de la lista.
print(my_ListaSort)


my_NumList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Ordering my_NumList: ")
my_NumList.sort()
print(my_NumList)
#OrderedList = my_NumList.sort()
#print(my_ListaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse=True)
print("De mayor a menor ", my_NumList)


##########TUPLAS##########
##########################

#Corresponde a una estructura similar a las listas, la diferencia está
#en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla_print
print("##################")
print("##################")
print("##################")
print("######TUPLAS######")
my_tupla = tuple(my_Lista)
print()
print()
print("my_tuple: ", my_tupla)

print(my_tupla[0]) #Imprime el elemento en dicha posición.
print(my_tupla[2])

#Evaluar si un elemento esta contenido en la tupla (devuelve un valor booleano)
print('Rojo' in  my_tupla)
print(my_tupla.count('Rojo'))

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

#Desempaquetado de tupla. se guardan los valores en orden de las varibales
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Día: ", dia, " - Mes: ", mes, " - Año: ", año)

#Convertir uan tupla en una lista
my_Lista2 = list(my_tupla)
print(my_Lista2)