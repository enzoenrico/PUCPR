# 1. (1.0) Segundo os conceitos de programação e da linguagem Python que aprendemos, relacione as colunas:
# ( a ) [“um”, “dois”, “três”] = Lista
# ( b ) != = Operador lógico
# ( c ) # = Comentários em Python
# ( d ) if...elif...else = Estrutura condicional
# ( e ) (0,) = Tupla
# ( f ) 10011001b = Número em formato binário
# ( g ) float = Tipo de dado
# ( h ) while = Estrutura de repetição
# ( i ) += = Operador acumulativo
# ( j ) { }  = Dicionário

# C, B, J, I, E, G, F, D, A, H

# 2. (1.0) Com suas palavras, defina o que é uma função. E explique: quais são as principais vantagens em usar
# funções em seu código?

# Funções são blocos de código autônomos que realizam tarefas definidas. Suas principais vantagens são:
# Modularidade: permitindo dividir o código em partes menores e independentes do bloco de código principal;
# Reutilização de código: evitando repetição usando blocos de código para realizar atividades que se repetem;
# Abstração: ocultando detalhes complexos;
# Facilidade de depuração: Onde ao isolar partes do código, a leitura se torna mais fácil e o código mais compreensivél, facilitando o trabalho em equipe.
# Funções tornam o código mais organizado, reutilizável, e fácil de se trabalhar

# 3. (1.0) Qual seria a principal vantagem, em termos de pesquisa de dados, em um sistema que faz uso de um
# dicionário como banco de dados no lugar de uma lista?

# A principal vantagem de usar um dicionário em vez de uma lista é sua capacidade de realizar pesquisas de forma mais eficiente.
# Enquanto em uma lista é necessário percorrer todos os elementos para encontrar um valor específico, em um dicionário é possível acessar diretamente o valor desejado por meio da chave da célula. Isso resulta em um tempo de busca mais rápido, especialmente quando existe uma base de dados grande. E as chaves dos dicionários também podem ser valores customizados para fácil acesso futuro.

# 4. (1.0) Defina, com suas palavras, o que é uma função recursiva
# Uma função recursiva é uma função que chama a sí mesma, assim, ao invés de ter uma função com um loop dentro, a função chama a sí mesma até que um parametro desejado seja cumprido, assim, retornando o valor desejado. Essa abordagem simplifica a lógica do código, permitindo resolver problemas de maneira eficiente.

# 5. (1.5) Crie uma função recursiva que inverte o texto dado como parâmetro. Usar no protótipo o seguinte
# cabeçalho:

def inverter(texto):
    if len(texto) == 0:  # Caso o input seja vazio
        return texto
    else:
        # itera por todas as letras, passando a última letra para a primeira posição
        return inverter(texto[1:]) + texto[0]


print(inverter('Texto'))  # output -> otxeT


# 6. (1.5) Uma matriz superior é aquela que tem os elementos da diagonal principal e todos acima dela iguais a
# 1, sendo que os demais são 0. Isto se dá pela definição:
# A = [Aij | 1 se j >= i, caso contrário 0]
# Exemplo: matriz diagonal superior de ordem 4:
# 𝐴4 = [
# 1 1 1 1
# 0 1 1 1
# 0 0 1 1
# 0 0 0 1
# ]
# Considerando esta definição acima, elabore um programa em Python que solicita ao usuário a ordem m da
# matriz, e gera uma matriz Am superior.

def gerarMatrizSuperior():
    tamanho = int(input("Digite a ordem da matriz: "))

    matriz = [[0] * tamanho for _ in range(tamanho)]  # Inicializa a matriz com zeros para alteração futura

    for i in range(tamanho):
        for j in range(i, tamanho):
            matriz[i][j] = 1

    return matriz

print(gerarMatrizSuperior())

# 7. (1.5) Criar um sistema composto por três funções:
# Função imprimir – recebe como parâmetro um texto t e usa a função print para imprimi-lo.
# Função reduzir – recebe um texto t e um número de caracteres n e devolve um texto composto pelo n
# primeiros caracteres de t.
# Função decidir – recebe um texto t e um número n. Caso tenha mais de n caracteres, chama a função reduzir(t,
# n), e imprime o retorno com a função imprimir(t). Caso contrário, chama direto a função imprimir(t). Obs.:
# os valores iniciais de t e n devem ser solicitados fora das funções ao usuário e, para realizar as devidas
# impressões, deve ser chamada a função decidir(t, n).
class Exercicio7():
    def imprimir(t):
        print(t)

    def reduzir(t, n):
        return t[:n]

    def decidir(t, n):
        if len(t) > n:
            texto_reduzido = Exercicio7.reduzir(t, n)
            Exercicio7.imprimir(texto_reduzido)
        else:
            Exercicio7.imprimir(t)

t = input("Digite um texto: ")
n = int(input("Digite o número de caracteres: "))

Exercicio7.decidir(t, n)


# 8. (1.5) Criar uma função em Python que recebe um dicionário. Esta função separa o dicionário em duas listas:
# chaves e valores, e retorna ambas em uma tupla.

def separar_dict(dict):
    chaves = list(dict.keys())
    valores = list(dict.values())
    return chaves, valores

# Exemplo de uso
dictExemplo = {"a": 1, "b": 2, "c": 3}
print(separar_dict(dictExemplo))
