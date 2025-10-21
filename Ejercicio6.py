#Escribe un programa que imprima la tabla de multiplicar de un número dado por el usuario, desde el 1 hasta el 10, utilizando un bucle for.

numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}") 
