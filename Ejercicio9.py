#Escribe un programa que pida al usuario un número y luego calcula su factorial utilizando un bucle while. El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.

num = int(input("Por favor de ingres un número entero positivo para calcular su factorial: "))

factorial = 1
contador = 1
while contador <= num:
    factorial *= contador
    contador += 1
