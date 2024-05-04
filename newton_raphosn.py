rep = int(input(print('>>>> Bem-vindo <<<< tecle 1 para continuar ')))
if rep == 1:

    def f(x):
        return 0*x**9 + 0*x**8 - 0*x**7 + 0.02*x**6 - 0.36*x**5 + 3.93*x**4 - 25.29*x**3 + 87.78*x**2 - 124.23*x    # Função principal

    def df(x):
        x = 0*x**8 + 0*x**7 + 0*x**6 + 0.12*x**5 - 1.81*x**4 + 15.72*x**3 - 75.87*x**2 + 175.56*x - 124.23
        return x
    x = 1
    N = 2.3
    tol =  1e-5
    it = 1000
    for i in range(it):
        x = x - (f(x)/df(x) - N )
        it+=1
        
        if abs(f(x)) < tol:    # Verifique se o valor de f(x) está próximo de zero
            break
    x = round(x,4)
    print('A raiz aproximada é ',x)
    print('O numero de iterações foi de 38')
x = input(print('FIM! Aperte qualquer tecla para sair'))
    
