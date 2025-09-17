sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)
print(num_cameras)
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
print(translations)

#Verificando un error:
powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
print(powers)

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)

my_empty_dictionary = {}
print(my_empty_dictionary)

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["cheesecake"] = 8
print("After", menu)
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"horses": 2}
print(animals_in_zoo)


#Agregando múltiples llaves:
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensors)

#Si quisieramos agregar 3 nuevas habitaciones, podríamos usar:
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("After", sensors)

###
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

## Sobreescribir Valores ##
#Sabemos que podemos agregar una llave usando la siguiente sintaxis:
menu["banana"] = 3
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["oatmeal"] = 5
print("After", menu)

# Note como el valor de "oatmeal" ahora ha cambiado a 5. 
scar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners)
print()
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After1", oscar_winners)
print()
oscar_winners["Best Picture"] = "Moonlight"
print("After2", oscar_winners)


###Comprensiones de Diccionarios (dict comprehension)
#Digamos que tenemos dos listas qe nos gustaría combinar a un
#diccionario, como una lista de estudiantes y una lista sobre sus estaturas
#en pulgadas:

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

#Python te permite crear un diccionario usando
# una "comprensión de diccionarios", con sintaxis:

zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents)

students = {key:value for key, value in zip(names, heights)}
#estudiantes ahora es {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
print(students)

#zip() combina dos listas en un iterador de tuplas con los elementos de la lsta emparejados. Esta comprensión de diccionario (dict comprehension):

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
print("After: ", plays)
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)