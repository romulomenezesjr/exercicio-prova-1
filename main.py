def q1():
    """
    Escreva um programa que solicite ao usuário um número e
    verifique se ele é par ou ímpar. Imprima uma mensagem informando o 
    resultado.
    """
    numero = int(input("Digite um número: "))
    if (numero % 2 == 0):
        print("Par")
    else:
        print("Impar")


def q2():
    """
    Dada a string use o operador de fatiamento para imprimir somente a metade final
    Para 'abcdef, imprima: 'def' 
          012345
    Para 'texto', imprima 'to'
          01234
    Para 'tempestade' imprima 'stade'
          1234567890
    """
    import math
    texto = input("Digite o texto: ")
    tamanho = len(texto) #6
    meio = math.ceil(tamanho / 2)  #3
    print(texto[meio:tamanho])

def q3():
    """
    Leia um número da entrada e imprima todos os 10 primeiros múltiplos dele na mesma linha
    """
    pass
def q4():
    """
    Escreva um programa que solicite ao usuário para digitar seu nome em letras
    minúsculas e, em seguida, imprima o nome com a primeira letra em maiúscula. Você
    não deve usar o método str.capitalize(). Preposições não devem ser iniadas com maiúsculo
    Exemplo: 
     - romulo junior - Romulo Junior
     - ze da manga - Ze da Manga
    """
    pass
def q5():
    """
    Verificação de Triângulo: Peça ao usuário o comprimento de três lados em uma única entrada
    e verifique se eles podem formar um triângulo. 
    Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.
    Exemplo:
        333: equilátero
        322: isosceles
        234: escaleno
    """
    pass

def q6():
    pass

def q7():
    pass

def q8():
    pass

def q9():
    pass

def q10():
    pass

if __name__ == "__main__":
    q2()