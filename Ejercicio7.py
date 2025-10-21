# Escribe un programa que pida al usuario un número entero positivo y luego imprime todos los números impares desde 1 hasta el número ingresado utilizando un bucle while.

num = int(input("Por favor digite un número entero positivo: "))
contador = 1
while contador <= num:
    if contador % 2 != 0:
        print(contador)
    contador += 1