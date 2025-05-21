# 🧪 Fundamentos Python II
# Listas, Tuplas, Diccionarios, Sets

# ------------------------------
# LISTAS
# ------------------------------

# ✨ Ejercicio 1: Lista de la compra
# Crea una lista con al menos 5 elementos. Muestra el primero y el último elemento.
print("---------------Ejercicio 1----------------")
lista = ["leche", "pan", "huevos", "carne", "verduras"]
print("The first element is: " + lista[0])
print("The last element is: " + lista[-1])

# ✨ Ejercicio 2: Añadir y eliminar
# Añade un nuevo elemento a la lista anterior y elimina otro. Imprime la lista actualizada.
lista.append("manzanas")
lista.remove("carne")
print(lista)

# ✨ Ejercicio 3: Ordenar números
# Crea una lista de números desordenados y ordénala de menor a mayor.
num_list = [5, 2, 9, 1, 5, 6]
num_list.sort()
print(num_list)
# ------------------------------
# TUPLAS
# ------------------------------

# ✨ Ejercicio 4: Coordenadas
# Crea una tupla con una coordenada (latitud, longitud) y muéstrala.
print("---------------Ejercicio 4----------------")
corodenadas_newyork = (40.7128, -74.0060)
print(f"Coordenadas de Nueva York: {corodenadas_newyork}")

# ✨ Ejercicio 5: Elemento fijo
# Crea una tupla de 3 elementos. Intenta cambiar uno y observa qué sucede.
print("---------------Ejercicio 5----------------")
tupla_ejericio5 = (1, 2, 3)
try:
    tupla_ejericio5[0] = 5
except TypeError as e:
    print(f"Error: {e}")
# ------------------------------
# DICCIONARIOS
# ------------------------------

# ✨ Ejercicio 6: Diccionario de usuario
# Crea un diccionario con las claves: nombre, edad, ciudad.
diccionario_ejercicio6 = {
    "nombre": "Nico",
    "edad": 27,
    "ciudad": "El Berron"}
# ✨ Ejercicio 7: Actualizar valores
# Cambia el valor de ciudad y añade una nueva clave llamada email.
print("---------------Ejercicio 7----------------")
diccionario_ejercicio6["ciudad"] = "Madrid"
diccionario_ejercicio6["email"] = "prueba@gmail.com"
print(diccionario_ejercicio6)
# ✨ Ejercicio 8: Iterar claves y valores
# Imprime cada clave y su valor en una línea distinta.
print("---------------Ejercicio 8----------------")
for clave, valor in diccionario_ejercicio6.items():
    print(f"{clave}: {valor}")
# ------------------------------
# SETS
# ------------------------------

# ✨ Ejercicio 9: Eliminar duplicados
# A partir de una lista con nombres repetidos, crea un set para mostrar solo los nombres únicos.
print("---------------Ejercicio 9----------------")
lista_nombres = ["Ana", "Luis", "Ana", "Pedro", "Luis"]
set_nombres = set(lista_nombres)
print(set_nombres)
# ✨ Ejercicio 10: Operaciones de conjuntos
# Dado dos sets A y B, muestra qué elementos están en A pero no en B.
print("---------------Ejercicio 10----------------")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(f"Elementos en A pero no en B: {A - B}")

# ------------------------------
# EXTRA
# ------------------------------

# 🌟 Ejercicio Extra: Mezcla total
# Crea un diccionario donde cada clave sea el nombre de una persona y el valor una lista de hobbies.
# Añade un nuevo hobby a una persona y muestra todos los hobbies de otra.
print("---------------Ejercicio Extra----------------")
diccionario_hobbies = {
    "Nico": ["programar", "leer"],
    "Ana": ["correr", "cocinar"],
    "Luis": ["futbol", "videojuegos"]
}
diccionario_hobbies["Nico"].append("pintar")
print(f"Hobbies de Ana: {diccionario_hobbies['Ana']}")
print(f"Hobbies de Nico: {diccionario_hobbies['Nico']}")