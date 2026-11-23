import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print("Média:", x.mean())
print("Desvio padrão:", x.std())
print("Valor minimo:", x.min())
print("Valor máximo:", x.max())

maiores_que_media = x[x > x.mean()]
print("Valores maiores que a média:", maiores_que_media)

print("Elementos ao quadrado:", x ** 2)  # Eleva cada elemento do array ao quadrado
print("Raiz quadrada:", np.sqrt(x))  # Calcula a raiz quadrada de cada elemento do array

quadrado = x ** 2
raiz = np.sqrt(x)
soma = quadrado + raiz
print("5 primeiros resultados:")
print(soma[:5])









