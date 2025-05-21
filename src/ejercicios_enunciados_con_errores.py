import csv
import os


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


# 🧪 Ejercicios – Consola + Buenas Prácticas (KISS, DRY, Excepciones)

# Ejercicio 1: Sistema de votaciones
# -----------------------------------
# Crea un programa en consola con las siguientes opciones:
# 1. Añadir película
# 2. Votar por una película
# 3. Mostrar resultados
# 4. Salir
# Si se intenta votar por una película no registrada, muestra error
# (usa try/except con KeyError).
# Usa funciones separadas por funcionalidad.
# (Bonus: guardar votos en un fichero CSV)
# (Bonus 2: leer votos de un fichero CSV al iniciar el programa)
clear_console()
print("---------------Ejercicio 1----------------")


print(
    "Bienvenido al sistema de votaciones\n"
    "1. Añadir película \n"
    "2. Votar por una película \n"
    "3. Mostrar resultados \n"
    "4. Salir \n"
)


films = {}


def read_votes_csv(file_name="votes.csv"):
    if os.path.exists(file_name):
        with open(file_name, mode="r", newline="", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                film = fila["Film"]
                votos = int(fila["Votes"])
                films[film] = votos
    else:
        print(
            "No se encontró un archivo de votaciones previo."
            "Se creará uno nuevo al votar."
        )


read_votes_csv()


def add_film(film):
    if film not in films:
        films[film] = 0
        print(f"Pelicula {film} añadida correctamente.")
        save_results_to_csv()
    else:
        print(f"Error: La pelicula {film} ya existe.")


def vote(film):
    try:
        films[film] += 1
        print(f"Voto registrado para la pelicula {film}.")
        save_results_to_csv()
    except KeyError:
        print(f"Error: La pelicula {film} no existe.")


def show_results():
    if films:
        print("Resultados de las votaciones:")
        for film, votes in films.items():
            print(f"{film}: {votes} votes.")
    else:
        print("No hay votos registrados.")


def save_results_to_csv(file_name="votes.csv"):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Film", "Votes"])
        for film in films:
            writer.writerow([film, films[film]])


while True:
    try:
        option = int(input("Selecciona una opción (1-4): "))
        if option == 1:
            film_name = input("Introduce el nombre de la película: ")
            add_film(film_name)
        elif option == 2:
            film_name = input("Introduce el nombre de la película a votar: ")
            vote(film_name)
        elif option == 3:
            show_results()
        elif option == 4:
            print("Saliendo del sistema de votaciones.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    except ValueError:
        print("Error: Debes introducir un número entre 1 y 4.")

# Ejercicio 2: Limpieza de datos crudos
# -------------------------------------
# Dada una lista de nombres con errores (espacios, mayúsculas, duplicados),
# crea una función que la limpie devolviendo una lista ordenada
# y sin duplicados.
# To-dos los nombres deben tener solo la primera letra en mayúscula.
# Muestra cuántos nombres únicos hay.
# 💡 Añade manejo de errores si algún elemento no es una cadena
# (TypeError o AttributeError)
clear_console()
print("---------------Ejercicio 2----------------")

names_list = [
    "  juan ",
    "maria",
    "Pedro",
    "maria",
    "JUAN",
    "  pedro  ",
    "Ana",
    "MARIMAR",
    123,
    None,
]


def clean_names(names):
    cleaned_names = []
    for name in names:
        try:
            if not isinstance(name, str):
                raise TypeError(f"Error: {name} no es una cadena.")
            cleaned_names.append(name.strip().capitalize())
        except TypeError as e:
            print(e)
            continue
        cleaned_names = list(set(cleaned_names))
        cleaned_names.sort()
    return cleaned_names


print(clean_names(names_list))


# Ejercicio 3: Analizador de texto
# --------------------------------
# Pide al usuario un párrafo.
# Luego:
# - Cuenta cuántas palabras contiene
# - Muestra cuántas veces aparece cada palabra
# - Muestra la palabra más repetida
# 💡 Controla que el texto no esté vacío. Usa ValueError.

print("---------------Ejercicio 3----------------")


def analyze_text(text):
    if not text.strip():
        raise ValueError("Error: El texto no puede estar vacio.")
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    most_common_word = max(word_count, key=word_count.get)
    return len(words), word_count, most_common_word


try:
    user_input = input("Introduce un párrafo: ")
    word_count, word_frequency, most_common_word = analyze_text(user_input)
    print(f"El párrafo contiene {word_count} palabras.")
    print("Frecuencia de palabras:", word_frequency)
    print(f"La palabra más repetida es '{most_common_word}'.")
except ValueError as e:
    print(e)


# Ejercicio 4: Simulador de inventario
# -------------------------------------
# Crea un sistema que permita gestionar productos en un inventario.
# Cada producto tiene nombre, stock y precio.
# Opciones:
# 1. Añadir producto
# 2. Actualizar stock
# 3. Eliminar producto
# 4. Ver inventario
# 💡 Usa try/except para validar entradas numéricas y para controlar
# si el producto no existe.

print("---------------Ejercicio 4----------------")


inventory = {}


def add_product(name, stock, price):
    try:
        if name in inventory:
            raise KeyError(f"Error: El producto {name} ya existe.")
        inventory[name] = {"stock": stock, "price": price}
        print(f"Producto {name} añadido correctamente.")
    except KeyError as e:
        print(e)


def update_stock(name, stock):
    try:
        if name not in inventory:
            raise KeyError(f"Error: El producto {name} no existe.")
        inventory[name]["stock"] += stock
        print(f"Stock actualizado para el producto {name}.")
    except KeyError as e:
        print(e)


def delete_product(name):
    try:
        if name not in inventory:
            raise KeyError(f"Error: El producto {name} no existe.")
        del inventory[name]
        print(f"El producto {name} se ha eliminado correctamente.")
    except KeyError as e:
        print(e)


def view_inventory():
    try:
        if not inventory:
            raise ValueError("Error: El inventario está vacio.")
        print("Inventario:")
        for name in inventory:
            stock = inventory[name]["stock"]
            price = inventory[name]["price"]
            print(f"{name}: {stock} unidades, precio {price}€")
    except ValueError as e:
        print(e)


while True:
    try:
        print(
            "Bienvenido al sistema de inventario\n"
            "1. Añadir producto \n"
            "2. Actualizar stock \n"
            "3. Eliminar producto \n"
            "4. Ver inventario \n"
            "5. Salir \n"
        )
        option = int(input("Selecciona una opcion (1-5): "))
        if option == 1:
            product_name = input("Introduce el nombre del producto: ")
            product_stock = int(input("Introduce el stock del producto: "))
            product_price = float(input("Introduce el precio del producto: "))
            add_product(product_name, product_stock, product_price)
        elif option == 2:
            product_name = input("Introduce el nombre del producto a actualizar: ")
            product_stock = int(input("Introduce el stock del producto a actualizar: "))
            update_stock(product_name, product_stock)
        elif option == 3:
            product_name = input("Introduce el nombre del producto a eliminar: ")
            delete_product(product_name)
        elif option == 4:
            view_inventory()
        elif option == 5:
            print("Saliendo del sistema de inventario.")
            break
        else:
            raise ValueError("Opción no válida. Inténtalo de nuevo.")
    except ValueError as e:
        print(e)


# Ejercicio 5: Generador de alias seguro
# ---------------------------------------
# Pide al usuario nombre y apellido, y genera un alias así:
# - 3 letras del apellido (mayúsculas)
# - 2 letras del nombre (minúsculas)
# - número aleatorio del 10 al 99
# - símbolo especial aleatorio
# 💡 Valida que el nombre y apellido tengan longitud suficiente (ValueError)

clear_console()

print("---------------Ejercicio 5----------------")

import random
import string


def generate_alias(name, surname):
    if len(name) < 2 or len(surname) < 3:
        raise ValueError(
            "Error: El nombre debe tener al menos 2 letras y el apellido al menos 3 letras."
        )

    surname_part = surname[:3].upper()
    name_part = name[:2].lower()
    random_number = random.randint(10, 99)
    special_char = random.choice(string.punctuation)
    alias = f"{surname_part}{name_part}{random_number}{special_char}"
    return alias


try:
    user_name = input("Introduce tu nombre: ")
    user_surname = input("Introduce tu apellido: ")
    alias = generate_alias(user_name, user_surname)
    print(f"Tu alias seguro es: {alias}")
except ValueError as e:
    print(e)


# Ejercicio 6: Comprobador de contraseñas seguras
# ------------------------------------------------
# Pide una contraseña al usuario.
# Valida que:
# - Tiene al menos 8 caracteres
# - Contiene mayúsculas, minúsculas y números
# 💡 Usa raise y excepciones personalizadas con mensajes explicativos.

print("---------------Ejercicio 6----------------")


class PasswordError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def validate_password(password):
    if len(password) < 8:
        raise PasswordError("Error: La contraseña debe tener al menos 8 caracteres.")
    if not any(char.isupper() for char in password):
        raise PasswordError(
            "Error: La contraseña debe contener al menos una mayúscula."
        )
    if not any(char.islower() for char in password):
        raise PasswordError(
            "Error: La contraseña debe contener al menos una minúscula."
        )
    if not any(char.isdigit() for char in password):
        raise PasswordError("Error: La contraseña debe contener al menos un número.")
    if not any(char in string.punctuation for char in password):
        raise PasswordError(
            "Error: La contraseña debe contener al menos un símbolo especial."
        )
    print("Contraseña segura.")


try:
    user_password = input("Introduce una contraseña: ")
    validate_password(user_password)
except PasswordError as e:
    print(e.message)


# 🌟 Reto Extra: Simulador de reservas de hotel
# ----------------------------------------------
# Habitaciones del 101 al 110. El usuario puede:
# 1. Ver habitaciones disponibles
# 2. Reservar habitación (introduciendo su nombre)
# 3. Cancelar reserva
# 4. Ver reservas confirmadas
# 5. Salir
# Las reservas se almacenan en un diccionario {habitacion: nombre}
# Usa funciones y control de errores con KeyError si la habitación no existe.
# (Bonus: mostrar mapa visual, reservas múltiples, carga inicial aleatoria)

print("-------------Ejercicio Extra--------------")
rooms = {
    101: None,
    102: None,
    103: None,
    104: None,
    105: None,
    106: None,
    107: None,
    108: None,
    109: None,
    110: None,
}


def show_available_rooms():
    avalible_rooms = [room for room, name in rooms.items() if name is None]
    if avalible_rooms:
        print("Habitaciones disponibles:", avalible_rooms)
    else:
        print("No hay habitaciones disponibles")


def reserve_room(room_input, name):
    try:
        room_numbers = [int(r.strip()) for r in room_input.split(",")]
        for room_number in room_numbers:
            if room_number not in rooms:
                print(f"Error: la habitación {room_number} no existe.")
            elif rooms[room_number] is not None:
                print(f"Error: la habitación {room_number} ya está reservada.")
            else:
                rooms[room_number] = name
                print(f"Reserva confirmada para la habitación {room_number} a nombre de {name}.")
    except ValueError:
        print("Error: formato de número de habitación no válido.")


def cancel_reservation(room_number):
    try:
        if room_number not in rooms:
            raise KeyError(f"Error: la habitacion {room_number} no existe.")
        if rooms[room_number] is None:
            raise ValueError(f"Error: la habitacion {room_number} no esta reservada.")
        rooms[room_number] = None
        print(f"Reserva cancelada para la habitacion {room_number}.")
    except KeyError as e:
        print(e)
    except ValueError as e:
        print(e)


def show_reservations():
    reserved_rooms = {room: name for room, name in rooms.items() if name is not None}
    if reserved_rooms:
        print("Reservas confirmadas:")
        for room, name in reserved_rooms.items():
            print(f"Habitacion {room}: {name}")
    else:
        print("No hay reservas confirmadas.")


# BONUS: mostrar mapa visual de habitaciones
def print_room_map():
    print("Mapa de habitaciones:")
    for room in sorted(rooms.keys()):
        status = "Libre" if rooms[room] is None else f"Reservada ({rooms[room]})"
        print(f"  Habitación {room}: {status}")


def load_random_reservations():
    nombres = ["Carlos", "Lucía", "Pedro", "María", "Sofía", "Raúl"]
    habitaciones_disponibles = list(rooms.keys())
    random.shuffle(habitaciones_disponibles)
    cantidad = random.randint(2, 5)
    for i in range(cantidad):
        room = habitaciones_disponibles[i]
        rooms[room] = random.choice(nombres)


load_random_reservations()

while True:
    try:
        print(
            "Bienvenido al sistema de reservas de hotel\n"
            "1. Ver habitaciones disponibles \n"
            "2. Reservar habitación \n"
            "3. Cancelar reserva \n"
            "4. Ver mapa de habitaciones \n"
            "5. Ver reservas confirmadas \n"
            "6. Salir \n"
        )
        option = int(input("Selecciona una opcion (1-6): "))
        if option == 1:
            show_available_rooms()
        elif option == 2:
            room_input = input("Introduce el número de habitación (o varios separados por comas): ")
            name = input("Introduce tu nombre: ")
            reserve_room(room_input, name)
        elif option == 3:
            room_number = int(input("Introduce el número de habitación a cancelar: "))
            cancel_reservation(room_number)
        elif option == 4:
            print_room_map()
        elif option == 5:
            show_reservations()
        elif option == 6:
            print("Saliendo del sistema de reservas.")
            break
        else:
            raise ValueError("Opción no válida. Inténtalo de nuevo.")
    except ValueError as e:
        print(e)
