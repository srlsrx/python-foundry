# 🧪 Fundamentos Python I – Enunciados

# ------------------------------
# TIPOS DE DATOS
# ------------------------------

# ✨ Ejercicio 1: ¿Qué tipo es?
# Declara las siguientes variables y usa type() para imprimir qué tipo de dato es cada una:
print("---------------Ejercicio 1----------------")
a = "Hola"
b = 25
c = 3.14
d = True
e = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print("------------------------------------------")
# ✨ Ejercicio 2: Conversión rápida
# Convierte la cadena "42" en número, súmale 8 y muestra el resultado.
# Luego convierte el número 100 en texto y muestra la frase:
# "Tu puntuación final es: 100"

# ------------------------------
# VARIABLES
print("---------------Ejercicio 2----------------")
num_string = "42"
sum = int(num_string) + 8
print(sum)
cien = 100
print("Tu puntuacion final es: " + str(cien))
print("------------------------------------------")
# ------------------------------

# ✨ Ejercicio 3: Nombres y saludos
# Crea una variable nombre y una variable edad.
# Imprime una frase como:
# Hola, me llamo X y tengo Y años.
print("---------------Ejercicio 3----------------")
nombre = "Nico"
edad = 27
print(f"Hola, me llamo {nombre} y tengo {edad} años.")
print("------------------------------------------")
print("---------------Ejercicio 4----------------")
# ✨ Ejercicio 4: Intercambio simple
# Tienes dos variables:
x = "gato"
y = "perro"
x, y = y, x
print("x: " + x)
print("y: " + y)
# Intercambia sus valores para que x valga "perro" y y valga "gato".
print("------------------------------------------")
# ------------------------------
# OPERADORES
# ------------------------------
print("---------------Ejercicio 5----------------")
# ✨ Ejercicio 5: Suma de la compra
# Declara tres precios:
pan = 1.50
leche = 1.24
huevos = 2.70
# Calcula el total y muestra: “El total de tu compra es de: 4,25€”
total = pan + leche + huevos
print(f"El total de tu compra es de : {total}€")
print("------------------------------------------")

print("---------------Ejercicio 6----------------")
# ✨ Ejercicio 6: ¿Par o impar?
# Pide al usuario un número con input() y di si es par o impar.
num = input("Escribe un numero: ")
if int(num) % 2 == 0:
    print ("El numero es par")
else: 
    print ("El numero es impar")
print("------------------------------------------")
# ------------------------------
# ESTRUCTURAS DE CONTROL
# ------------------------------
print("---------------Ejercicio 7----------------")
# ✨ Ejercicio 7: ¿Mayor de edad?
# Pide la edad al usuario. Si tiene 18 o más, muestra “Puedes entrar”.
# Si no, muestra “Acceso denegado”.
edad = input("Escribe tu edad: ")
if int(edad) >= 18:
    print("Puedes entrar")
else: 
    print("Acceso denegado")
print("------------------------------------------")

print("---------------Ejercicio 8----------------")
# ✨ Ejercicio 8: Elige una opción
# Pide al usuario que elija una opción:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesión
# Y muestra un mensaje distinto para cada caso.
print("Elige una opción:")
print("1. Ver perfil")
print("2. Editar perfil")
print("3. Cerrar sesión")
option = input("Escribe el numero de la opción elegida: ")
if option == "1":
    print("Has elegido ver perfil")
elif option == "2":
    print("Has elegido editar perfil")
elif option == "3":
    print("Has elegido cerrar sesión")
else: 
    print("Opcion no valida")
print("------------------------------------------")
# ------------------------------
# EXTRA: TIPOS + CONDICIONAL
# ------------------------------
print("---------------Ejercicio 9----------------")
# ✨ Ejercicio 9: Detector de tipos raros
# Pide al usuario que escriba cualquier cosa.
# Muestra:
# - Si es un número entero: “Has escrito un número entero”
# - Si es un número decimal: “Has escrito un número decimal”
# - Si es un texto: “Parece que es una cadena de texto”
# - Si no puedes adivinar el tipo: “No sé qué es esto 😵‍💫”
# Usa try/except para intentar convertir a int() o float().
data = input("Write something here: ")
try:
    int(data)
    print("You have written an integer")
except ValueError:
    try:
        float(data)
        print("You have written a decimal number")
    except ValueError:
        if isinstance(data, str):
            print("You have written a string")
        else:
            print("I don't know what this is")
print("------------------------------------------")
# ------------------------------
# OPERADORES + CONDICIONALES + VARIABLES
# ------------------------------
print("---------------Ejercicio 10---------------")
# ✨ Ejercicio 10: Calculadora con menú
# Pide dos números y muestra este menú:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# Según la opción elegida, haz la operación y muestra el resultado.
# Bonus: si elige dividir y el segundo número es 0, muestra “No se puede dividir por cero”.
print("Calculator")
num1 = input("Write the first number: ")
num2 = input("Write the second number: ")
print("Choose an option:")
print("1. Sum")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
option = input("Write the number of the chosen option: ")
if option == "1":
    result = print("The result is: " + str(int(num1) + int(int(num2))))
elif option == "2":
    result = print("The result is: " + str(int(num1) - int(int(num2))))
elif option == "3":
    result = print("The result is: " + str(int(num1) * int(int(num2))))
elif option == "4":
    if(int(num1) == 0 or int(num2) == 0):
        print("You can't divide by zero")
    else:
        result = print("The result is: " + str(int(num1) / int(int(num2))))
print("------------------------------------------")
# ------------------------------
# ESTRUCTURA DE CONTROL CON RANGOS
# ------------------------------
print("---------------Ejercicio 11---------------")
# ✨ Ejercicio 11: Clasificador de edad
# Pide al usuario su edad y clasifícalo:
# - Menor de 3: “Bebé”
# - Entre 3 y 12: “Infancia”
# - Entre 13 y 17: “Adolescencia”
# - Entre 18 y 64: “Adulto”
# - 100 o más: “Senior”
edad= input("Write your age: ")
if int(edad) < 3:
    print("Baby")
elif int(edad) >= 3 and int(edad) <= 12:
    print("Child")
elif int(edad) >= 13 and int(edad) <= 17:
    print("Teen")
elif int(edad) >= 18 and int(edad) <= 64:
    print("Adult")
elif int(edad) >= 100:
    print("Senior")
print("------------------------------------------")