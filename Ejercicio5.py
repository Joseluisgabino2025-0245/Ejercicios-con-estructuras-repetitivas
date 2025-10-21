#Escribe un programa que pida al usuario un número entero y luego imprime todos los números desde ese número hasta el 0 en orden descendente utilizando un bucle while.

num = int(input("Digite un número entero por favor: "))
while num >= 0:
    print(num)
    num -= 1 
