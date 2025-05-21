# 🧪 Fundamentos Python III – Funciones

# ------------------------------
# ✨ Ejercicio 1: Saludo básico
# Objetivo: Aprender a definir y llamar funciones
# Crea una función llamada saludar() que imprima: "¡Hola, bienvenido/a!"
# Luego llama a la función una vez para comprobar que funciona.
print("---------------Ejercicio 1----------------")


def saludar():
    print("Hola, bienvenido/a!")


saludar()
print("------------------------------------------")


# ------------------------------
# ✨ Ejercicio 2: Saludo personalizado
# Objetivo: Trabajar con parámetros
# Crea una función llamada saludar_persona(nombre)
#  que imprima: "Hola, [nombre]!"
# Llama a la función dos veces con diferentes nombres.
print("---------------Ejercicio 2----------------")


def saludar_persona(nombre):
    print(f"Hola, {nombre}!")


saludar_persona("Nico")
print("-------------------------------------------")


# ------------------------------
# ✨ Ejercicio 3: Suma fácil
# Objetivo: Usar parámetros y return
# Crea una función llamada sumar(a, b) que devuelva la suma de dos números.
# Guarda el resultado en una variable y muéstralo con print().
print("---------------Ejercicio 3----------------")


def sumar(a, b):
    return a + b


res = sumar(2, 9)
print(f"La suma es: {res}")
print("-------------------------------------------")


# ------------------------------
# ✨ Ejercicio 4: ¿Par o impar?
# Objetivo: Usar lógica dentro de una función
# Escribe una función es_par(numero) que devuelva True si el número es par y
# False si es impar.
# Pruébala con varios números y muestra el resultado.
print("---------------Ejercicio 4----------------")


def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(es_par(4))
print(es_par(5))
print(es_par(6))
print(es_par(7))
print("-------------------------------------------")


# ------------------------------
# ✨ Ejercicio 5: Mensaje con formato
# Objetivo: Devolver una cadena con formato
# Crea una función llamada mensaje(nombre, edad) que devuelva una frase como:
# "Me llamo Marta y tengo 30 años."
# Usa return y luego muestra el mensaje con print().
print("---------------Ejercicio 5----------------")


def mensaje(nombre, edad):
    return f"Me llamo {nombre} y tengo {edad} años."


print(mensaje("Nico", 27))
print("____________________________________________")

# ------------------------------
# ✨ Ejercicio 6: Calculadora simple
# Objetivo: Practicar varias funciones juntas
# Crea 4 funciones: sumar(a, b), restar(a, b), multiplicar(a, b), dividir(a, b)
# Llama a cada una con un par de números y muestra los resultados.
# Bonus: en dividir(), si el segundo número es 0, devuelve "No se puede
# dividir por cero"
print("---------------Ejercicio 6----------------")


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if a == 0 or b == 0:
        return "No se puede dividir por cero"
    else:
        return a / b


print(f"Suma: {sumar(5, 3)}")
print(f"Resta: {restar(5, 3)}")
print(f"Multiplicación: {multiplicar(5, 3)}")
print(f"División: {dividir(5, 3)}")
print(f"División: {dividir(5, 0)}")
print("____________________________________________")

# ------------------------------
# ✨ Ejercicio 7: Edad en el futuro
# Objetivo: Usar return con operaciones
# Escribe una función llamada edad_futura(edad_actual, años) que calcule la
# edad que tendrás después de X años.
print("---------------Ejercicio 7----------------")


def edad_futura(edad_actual, años):
    return edad_actual + años


print(f"Tu edad en 10 años será: {edad_futura(27, 10)}")
print(f"Tu edad en 20 años será: {edad_futura(27, 20)}")
print(f"Tu edad en 30 años será: {edad_futura(27, 30)}")
print("____________________________________________")

# ------------------------------
# ✨ Ejercicio 8: Media de 3 números
# Objetivo: Trabajar con números y return
# Crea una función llamada calcular_media(a, b, c)
# que devuelva la media de 3 números.
# Prueba la función y muestra el resultado con print().
print("---------------Ejercicio 8----------------")


def calcular_media(a, b, c):
    return (a + b + c) / 3


print(calcular_media(2, 4, 6))
print(calcular_media(1, 2, 3))
print(calcular_media(10, 20, 30))
print("____________________________________________")

# ------------------------------
# ✨ Ejercicio 9: Mostrar menú (sin lógica)
# Objetivo: Separar la presentación de la lógica
# Escribe una función llamada mostrar_menu() que imprima un pequeño menú como:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesiónç
print("---------------Ejercicio 9----------------")


def mostrar_menu():
    print("1. Ver perfil")
    print("2. Editar perfil")
    print("3. Cerrar sesión")


mostrar_menu()
print("____________________________________________")

# ------------------------------
# 🌟 Reto Final: Generador de contraseñas

# Crea una función llamada generar_contraseña(longitud)
# que devuelva una contraseña aleatoria con la longitud especificada.

# La contraseña debe contener una mezcla de:
# - letras minúsculas (a-z)
# - letras mayúsculas (A-Z)
# - números (0-9)
# - símbolos como !, @, #, $, %, &, *

# Ejemplo de uso:
# contraseña = generar_contraseña(12)
# print(contraseña)  # -> A2c$e9#Tq&7L

# Bonus:
# - Usa la librería random
# - Controla que la longitud mínima sea 8 caracteres
# - Añade un mensaje de advertencia si se pide menos de 8

print("--------------Ejercicio Final--------------")


def generar_contraseña(longitud):
    import random
    import string

    if longitud < 8:
        return "La longitud mínima es de 8 caracteres."
    else:
        caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"
        contrasena = "".join(random.choice(caracteres) for i in range(longitud))
        return contrasena


inp_pssw = input("¿Cuántos caracteres quieres en tu contraseña? ")
print(generar_contraseña(int(inp_pssw)))

print("____________________________________________")
