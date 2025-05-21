# 🌟 Reto: Gestor de contactos

# 🎯 Objetivo:
# Crear una pequeña aplicación en consola que permita al usuario
# almacenar, mostrar y buscar contactos usando listas y diccionarios.

# Instrucciones:

# 1. Añadir un contacto:
#    - Pide al usuario el nombre, edad y ciudad.
#    - Guarda el contacto en una lista como un diccionario.

# 2. Mostrar todos los contactos:
#    - Recorre la lista y muestra los datos en el formato:
#      Nombre: Marta – Edad: 30 – Ciudad: Oviedo

# 3. Buscar por nombre:
#    - Pide un nombre y muestra el contacto si existe.

# 4. Salir:
#    - Si el usuario elige la opción 4, termina el programa.

# 💡 Menú sugerido:
# ¿Qué quieres hacer?
# 1. Añadir contacto
# 2. Ver contactos
# 3. Buscar por nombre
# 4. Salir

print("---------------CONTACT MANAGER---------------")
print("What do you want to do?")
print("1. Add contact")
print("2. View contacts")
print("3. Search by name")
print("4. Exit")
print("---------------------------------------------")
dictionary_contacts = [
    {
        "name": "Marta",
        "age": 30,
        "city": "Oviedo"
    },
    {
        "name": "Luis",
        "age": 25,
        "city": "Madrid"
    },
    {
        "name": "Ana",
        "age": 28,
        "city": "Barcelona"
    }
]
def add_contact():
    name = input("Enter name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")
    contact = {"name": name, "age": age, "city": city}
    dictionary_contacts.append(contact)
    print(f"Contact {name} added.")
def view_contacts():
    if not dictionary_contacts:
        print("No contacts available.")
    else:
        for contact in dictionary_contacts:
            print(f"Name: {contact['name']} - Age: {contact['age']} - City: {contact['city']}")
def search_contact():
    name = input("Enter the name to search: ")
    found = False
    for contact in dictionary_contacts:
        if contact["name"].lower() == name.lower():
            print(f"Contact found: Name: {contact['name']} - Age: {contact['age']} - City: {contact['city']}")
            found = True
            break
    if not found:
        print("Contact not found.")
first_option = input("Choose an option: ")
if first_option == "1":
    add_contact()
elif first_option == "2":
    view_contacts()
elif first_option == "3":
    search_contact()
elif first_option == "4":
    print("Exiting the program.")
else:
    print("Invalid option. Please try again.")