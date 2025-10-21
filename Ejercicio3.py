#Escribe un programa que pida al usuario un número entero positivo. El programa debe contar cuántos dígitos tiene el número utilizando un bucle while.

num = int(input("Ingresa un número entero positivo: "))
contador_digitos = 0

while num > 0:
    num //= 10
    contador_digitos += 1

print("El número tiene", contador_digitos, "dígitos.") 
