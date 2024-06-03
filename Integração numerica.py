# Definição da função
def f(x):
    return x*x
# Dados de entrada
a = 1
b = 3
n = 4 # Definindo um número inteiro de subintervalos
h = (b - a) / n

xm = a+h/2
# Inicializando as somas
soma_inferior = 0
soma_superior = 0
soma_media = 0

# Aproximação Inferior
for i in range(n-1):
    xi = f(a) + h
    soma_inferior += xi
    

# Aproximação Superior
for i in range(n-1):
    xs = f(a + h) 
    soma_superior += xs
    

# Aproximação dos Pontos Médios
for i in range(n-1):
    xm = f(a+h/2) + h
    soma_media += xm
    print(soma_media)
 

# Multiplicando pela largura dos subintervalos
aprox_inferior = h * soma_inferior + f(a)
aprox_superior = h * soma_superior + f(b)
aprox_media = h * soma_media + f(a+h/2)

# Imprimindo os resultados
print(f'Aproximação Inferior: {aprox_inferior:.4f}')
print(f'Aproximação Superior: {aprox_superior:.4f}')
print(f'Aproximação dos Pontos Médios: {aprox_media:.4f}')
print({soma_media})
print(h)
print(a)
