
def f(x):
    return  0*x**9 + 0*x**8 - 0*x**7 + 0.02*x**6 - 0.36*x**5 + 3.93*x**4 - 25.29*x**3 + 87.78*x**2 - 124.23*x

# Dados de entrada
a = 1
b = 38
n = 100000  # Definindo um número inteiro de subintervalos
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

#Valor médio
integral = 177.67
valor_medio = integral / b-a

# Multiplicando pela largura dos subintervalos
aprox_inferior = h * soma_inferior
aprox_superior = h * soma_superior
aprox_media = h * soma_media

# Imprimindo os resultados
print('==============================================')
print(f'Aproximação Inferior: {aprox_inferior:.4f}')
print(f'Aproximação Superior: {aprox_superior:.4f}')
print(f'Aproximação dos Pontos Médios: {aprox_media:.4f}')
print(f'O valor médio da função é {valor_medio:.4f}')
print('==============================================')
