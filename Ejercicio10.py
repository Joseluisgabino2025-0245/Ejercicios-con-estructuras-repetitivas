#Escribe un programa que pida al usuario ingresar una contraseña y repita la solicitud mientras la contraseña ingresada sea incorrecta. El programa debe continuar hasta que el usuario ingrese la contraseña correcta. Utiliza una estructura while para simular un do while.

contraseña_correcta = "211025"
intento = "∞"

while True:
    intento = input("Ingresa la contraseña: ")
    if intento == contraseña_correcta:
        print("Contraseña correcta. Acceso permitido.")
        break
    else:
        print("Contraseña incorrecta. Ingresa la correcta por favor.")
