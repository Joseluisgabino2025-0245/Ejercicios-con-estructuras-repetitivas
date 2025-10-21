#Escribe un programa que imprime la serie de Fibonacci hasta el enésimo término, donde el valor de n lo ingresa el usuario, utilizando un bucle for.

n = int(input("Digite el número de términos de la serie Fibonacci que desea ver si puedes: "))

a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b
