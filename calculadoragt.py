import matplotlib.pyplot as plt
import numpy as np

def mostrarCalculadora(textoDeDentro: str):
    linhas = textoDeDentro.split("\n")
    padding = 2
    maximoCaracteresPorLinha = 14
    linhasCalculadora = []

    linhas = [linha.strip() for linha in linhas]
    for linha in linhas:
        if (len(linha) <= maximoCaracteresPorLinha):
            linhasCalculadora.append(linha)
            continue
        palavras = linha.split(" ")
        palavras = [palavra.strip() for palavra in palavras]
        linhaAtual = ""
        for palavra in palavras:
            if (len(linhaAtual + palavra) > maximoCaracteresPorLinha):
                linhasCalculadora.append(linhaAtual)
                linhaAtual = palavra + " "
            else:
                linhaAtual += palavra + " "
        linhasCalculadora.append(linhaAtual)

    print(" " + "_" * maximoCaracteresPorLinha + 2 * padding * "_")
    for _ in range(padding):
        print("|" + " " * maximoCaracteresPorLinha + 2 * padding * " " + "|")
    for linha in linhasCalculadora:
        print("|" + padding * " " +
              linha.center(maximoCaracteresPorLinha, " ") + padding * " " + "|")
    for _ in range(padding):
        print("|" + padding * " " + " " *
              maximoCaracteresPorLinha + padding * " " + "|")
    print("|" + "_" * maximoCaracteresPorLinha + 2 * padding * "_" + "|")

calculator = """
 _________________
|  _____________  |
| |_____________| |
| |             | |
| | x² √  CE  C | |
| | 7  8  9   / | |
| | 4  5  6   * | |
| | 1  2  3   - | |
| | 0  .  =   + | |
| |_____________| |
|_________________|
    """
print(calculator)


def soma(n1, n2):
    return n1 + n2


def subtracao(n1, n2):
    return n1 - n2


def multiplicacao(n1, n2):
    return n1 * n2


def divisao(n1, n2):
    return n1 / n2


def linear(n1, n2, n3):
    return n1 * n2 + n3


def plot_linear(n1, n2):
    axisX = np.linspace(-10, 10, 100)
    axisY = linear(axisX, n1, n2)
    plt.plot(axisX, axisY, marker='o')
    plt.title(f"Gráfico da função linear {n1}x + {n2}")
    plt.xlabel('x')
    plt.ylabel('y')   
    plt.grid(True)
    plt.show()
    

def exponencial(n1, n2):
    if n2 == 0:
        return 1
    else:
        return n1 ** n2 


def plot_exponencial(n1, n2):
    x = np.linspace(-6, 6, 100)
    y = exponencial(x, n1 ** n2)
    
    plt.plot(x, y)
    plt.title("Função exponencial")
    plt.xlabel("Expoente")
    plt.ylabel("Valor")
    plt.grid(True)
    plt.show()    


def funcao_quadratica(n1, n2, n3, n4):
    return n1 * n2 ** 2 + n2 * n4 + n3
    

def plot_quadratica(n1, n2, n3):
    x = np.linspace(-10, 10, 100)
    y = funcao_quadratica(x, n1, n2, n3)
    
    plt.plot(x, y)
    plt.title('Função Quadratica')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()
    
def calcular_raizes(n1, n2, n3):
    delta = n2**2 - 4 * n1 * n3
    if delta > 0:
        x1 = (-n2 + np.sqrt(delta) / (2 * n1))
        x2 = (-n2 - np.sqrt(delta) / (2 * n1))
        return x1, x2
    elif delta == 0:
        x = -n2 / (2 * n1)
        return x
    else:
        return('não tem raiz real')
        

def fatorial(n):
    if n < 0:
            return "erro não é possível calcular o fatorial de um número negativo"
    elif n == 0:
            return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
                resultado *= i
        return resultado


def plot_fatorial(n):
    x = list(range(n + 1))
    y = [fatorial(i) for i in x]
    plt.plot(x, y, marker= 'x', linestyle= '-')
    plt.title('Gráfico Fatorial')
    plt.xlabel('Número')
    plt.ylabel('Fatorial')
    plt.grid(True)
    plt.show()
    

def print_calculator():

    mostrarCalculadora("""Inicie uma operação       
                                
    1: Básicas
    2: Funções 
    3: Sair""")


def print_basica():
    mostrarCalculadora("""Escolha sua  Opção     
                       
  1: Soma       
  2: Subtração  
  3: Multip.   
  4: Divisão    
  5: Voltar""")


def print_funcoes():
    mostrarCalculadora("""Escolha sua Função    
                                 
      1: Exponencial        
      2: Quadrática    
      3: Linear    
      4: Fatorial
      5. Voltar""")


def init():
    print_calculator()

    escolha = int(input("\nEscolha uma opção para iniciar: "))

    while escolha != 3:
        if escolha == 1:
            print_basica()

            categoria = int(input("\nEscolha uma categoria: "))
            while categoria != 5:

                if categoria == 1:
                    print("\nVocê escolheu SOMA")
                    n1 = float(input("\nDigite seu primeiro número: "))
                    n2 = float(input("\nDigite seu segundo número: "))
                    n3 = n1 + n2
                    print(f"{n1} + {n2} é: {n3}")
                    break

                elif categoria == 2:
                    print("\nVocê escolheu SUBTRAÇÃO")
                    n1 = float(input("\nDigite seu primeiro número: "))
                    n2 = float(input("\nDigite seu segundo número: "))
                    n3 = n1 - n2
                    print(f"{n1} - {n2} é: {n3}")
                    break

                elif categoria == 3:
                    print("\nVocê escolheu MULTIPLICAÇÃO")
                    n1 = float(input("\nDigite seu primeiro número: "))
                    n2 = float(input("\nDigite seu segundo número: "))
                    n3 = n1 * n2
                    print(f"{n1} x {n2} é: {n3}")
                    break

                elif categoria == 4:
                    print("\nVocê escolheu DIVISÃO")
                    n1 = float(input("\nDigite seu primeiro número: "))
                    n2 = float(input("\nDigite seu segundo número: "))
                    n3 = n1 / n2
                    print(f"{n1} / {n2} é: {n3}")
                    break

                elif categoria == 5:
                    print_basica()

        elif escolha == 2:
            print_funcoes()

            funcao = int(input("\nEscolha uma função: "))

            while funcao != 5:

                if funcao == 1:
                    print("\nVocê escolheu a função EXPONENCIAL (a ** x)")
                    n1 = int(input("\nDigite seu primeiro número: "))
                    n2 = int(input("Digite seu segundo número: "))
                    n3 = exponencial(n1, n2)
                    print(f"\nO resultado é: {n3}")
                    print(plot_exponencial(n1, n2))
                    break
                    

                elif funcao == 2:
                    print("\nVocê escolheu a função QUADRÁTICA (a * x ** 2 + b * x + c)")
                    n1 = int(input("\nDigite seu primeiro número: "))
                    n2 = int(input("Digite seu segundo número: "))
                    n3 = int(input("Digite seu terceiro número: "))
                    n4 = int(input("Digite seu quarto número: "))
                    n5 = funcao_quadratica(n1, n2, n3, n4)
                    print(f"\nO resultado é: {n5}")
                    print(plot_quadratica(n1, n2, n3))
                    break

                elif funcao == 3:
                    print("\nVocê escolheu a função LINEAR f(x) = (a * x + b)")
                    
                    break

                elif funcao == 4:
                    print("\nVocê escolheu a função FATORIAL f(x) = (a * x + b)")
                    
                    break

                elif funcao == 5:
                    print_funcoes()

        elif escolha == 3:
            break
        print_calculator()

        escolha = int(input("\nEscolha uma opção para iniciar: "))


init()