import pandas as pd
import math
import funcoes as f

def bisseccao(f, a, b, iteracoes, eps=1e-6):
    dados = {
        "Iteração": [],
        "a": [],
        "f(a)": [],
        "b": [],
        "f(b)": [],
        "c": [],
        "f(c)": [],
        "f(a) * f(c)": [],
        "f(c) * f(b)": [],
        "Erro absoluto": [],
        "Erro relativo": [],
        "Critério de parada": []
    }

    if f(a) * f(b) >= 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos")

    ant = 0
    for i in range(iteracoes):
        c = (a + b) / 2
        fa = f(a)
        fb = f(b)
        fc = f(c)

        fac = 'POS' if fa * fc > 0 else 'NEG'
        fcb = 'POS' if fc * fb > 0 else 'NEG'

        erro_absoluto = abs(c - ant) 
        erro_relativo = abs(erro_absoluto / c) if c != 0 else float('inf')
        criterio_de_parada = math.log((2-1)/erro_relativo)/math.log(2)

        ant = c
        dados["Iteração"].append(i)
        dados["a"].append(a)
        dados["f(a)"].append(fa)
        dados["b"].append(b)
        dados["f(b)"].append(fb)
        dados["c"].append(c)
        dados["f(c)"].append(fc)
        dados["f(a) * f(c)"].append(fac)
        dados["f(c) * f(b)"].append(fcb)
        dados["Erro absoluto"].append(erro_absoluto)
        dados["Erro relativo"].append(erro_relativo)
        dados["Critério de parada"].append(criterio_de_parada)


        # Calcula o número de casas decimais de eps
        decimais = abs(math.floor(math.log10(eps)))

        # Verifica se o erro absoluto ou relativo é menor ou igual a eps
        if round(erro_absoluto, decimais) <= eps: print("erro absoluto atingiu na iteração ", i) 
        if round(erro_relativo, decimais) <= eps: print("erro relativo atingiu na iteração ", i) 

        if fa * fc < 0:
            b = c
        else:
            a = c

    tabela = pd.DataFrame(dados)
    return tabela

def newton(f, df, x0, iteracoes, eps=1e-6):
    dados = {
        "Iteração": [],
        "x": [],
        "f(x)": [],
        "f'(x)": [],
        #"x_(k+1)": [],
        "Erro absoluto": [],
        "Erro relativo": [],
        "F(Xn)": [],
        "Critério de parada": []
    }

    ant = 0
    for i in range(iteracoes):
        fx = f(x0)
        dfx = df(x0)
        x1 = x0 - (fx / dfx)

        erro_absoluto = abs(x0 - ant)
        erro_relativo = erro_absoluto / abs(x0)
        criterio_de_parada = math.log((2-1)/erro_relativo)/math.log(2)

        fxn = abs(f(x0))
        ant = x0

        dados["Iteração"].append(i)
        dados["x"].append(x0)
        dados["f(x)"].append(round(fx, 7)) # funcao em potencia bota 4
        dados["f'(x)"].append(dfx)
        #dados["x_(k+1)"].append(x1)
        dados["Erro absoluto"].append(erro_absoluto)
        dados["Erro relativo"].append(erro_relativo)
        dados["F(Xn)"].append(round(fxn, 7)) # funcao em potencia bota 4
        dados["Critério de parada"].append(criterio_de_parada)


        # Calcula o número de casas decimais de eps
        decimais = abs(math.floor(math.log10(eps)))

        # Verifica se o erro absoluto ou relativo é menor ou igual a eps
        if round(erro_absoluto, decimais) <= eps: print("erro absoluto atingiu na iteração ", i) 
        if round(erro_relativo, decimais) <= eps: print("erro relativo atingiu na iteração ", i) 

        x0 = x1


    tabela = pd.DataFrame(dados)
    return tabela

def secante(f, a, b, iteracoes, eps=1e-6):
    dados = {
        "Iteração": [],
        "a": [],
        "f(a)": [],
        "b": [],
        "f(b)": [],
        "ze": [],
        "f(ze)": [],
        "Erro absoluto": [],
        "Erro relativo": [],
        "F(Xn)": [],
        "Critério de parada": []
    }

    ant = 0
    for i in range(iteracoes):
        ze = (a * f(b) - b * f(a)) / (f(b) - f(a))

        erro_absoluto = abs(ze - ant)
        erro_relativo = erro_absoluto / abs(ze)
        criterio_de_parada = math.log((2-1)/erro_relativo)/math.log(2)

        fxn = abs(f(ze))
        ant = ze

        dados["Iteração"].append(i)
        dados["a"].append(a)
        dados["f(a)"].append(f(a))
        dados["b"].append(b)
        dados["f(b)"].append(f(b))
        dados["ze"].append(ze)
        dados["f(ze)"].append(f(ze))
        dados["Erro absoluto"].append(erro_absoluto)
        dados["Erro relativo"].append(erro_relativo)
        dados["F(Xn)"].append(fxn)
        dados["Critério de parada"].append(criterio_de_parada)

        # Calcula o número de casas decimais de eps
        decimais = abs(math.floor(math.log10(eps)))

        # Verifica se o erro absoluto ou relativo é menor ou igual a eps
        if round(erro_absoluto, decimais) <= eps: print("erro absoluto atingiu na iteração ", i) 
        if round(erro_relativo, decimais) <= eps: print("erro relativo atingiu na iteração ", i) 

        if f(a) * f(ze) < 0:
            b = ze
        else:
            a = ze

    tabela = pd.DataFrame(dados)
    return tabela

def menu():

    print("Escolha a formula:")
    print("1. Ln")
    print("2. Exponencial")
    func_escolha = int(input("Digite o número da função desejada: "))
    if func_escolha == 1:
        func = f.ln1f
        df_func = f.ln1df
    elif func_escolha == 2:
        func = f.exp1f
        df_func = f.exp1df

    print("Escolha o método numérico:")
    print("1. Bissecção")
    print("2. Newton")
    print("3. Secante")
    escolha = int(input("Digite o número do método desejado: "))

    if escolha == 1:
        a = float(input("Digite o valor inicial a: "))
        b = float(input("Digite o valor inicial b: "))
        iteracoes = int(input("Digite o número de iterações: "))
        eps = float(input("Digite o erro (eps): "))
        print("\n")
        tabela = bisseccao(func, a, b, iteracoes, eps)
        print(tabela)
    elif escolha == 2:
        x0 = float(input("Digite o valor inicial x0: "))
        iteracoes = int(input("Digite o número de iterações: "))
        eps = float(input("Digite o erro (eps): "))
        print("\n")
        tabela = newton(func, df_func, x0, iteracoes, eps)
        print(tabela)
    elif escolha == 3:
        a = float(input("Digite o valor inicial a: "))
        b = float(input("Digite o valor inicial b: "))
        iteracoes = int(input("Digite o número de iterações: "))
        eps = float(input("Digite o erro (eps): "))
        print("\n")
        tabela = secante(func, a, b, iteracoes, eps)
        print(tabela)
    else:
        print("Método inválido. Tente novamente.")

# Chamando o menu
menu()
