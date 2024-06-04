# Definição da função
def f(x):
    return x * x

# Dados de entrada
a = 1
b = 3
n = 4  # Definindo um número inteiro de subintervalos
h = (b - a) / n

# Inicializando as somas
soma_inferior = 0
soma_superior = 0
soma_media = 0

# Aproximação Inferior
for i in range(n):
    xi = a + i * h
    soma_inferior += f(xi)

# Aproximação Superior
for i in range(1, n + 1):
    xs = a + i * h
    soma_superior += f(xs)

# Aproximação dos Pontos Médios
for i in range(n):
    xm = a + (i + 0.5) * h
    soma_media += f(xm)

# Multiplicando pela largura dos subintervalos
aprox_inferior = h * soma_inferior
aprox_superior = h * soma_superior
aprox_media = h * soma_media

# Imprimindo os resultados
print(f'Aproximação Inferior: {aprox_inferior:.4f}')
print(f'Aproximação Superior: {aprox_superior:.4f}')
print(f'Aproximação dos Pontos Médios: {aprox_media:.4f}')
