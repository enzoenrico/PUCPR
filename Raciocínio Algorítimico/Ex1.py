def ex1():
    n = input('Escreva um número:\n')
    m = input('Escreva um número:\n')
    print(f"Sua soma é : {m + n}")
    

def ex2():
    n = input('Insira seu ano de nascimento')
    print(f"Você tem: {abs(2023 - n)}")

def ex3():
    nm = input('Insira o nome de sua matéria')
    n1 = input("Insira a nota do 1 bim")
    n2 = input("Insira a nota do 2 bim")
    n3 = input("Insira a nota do 3 bim")
    n4 = input("Insira a nota do 4 bim")

    print(f'A sua média em {nm} é: {(n1 + n2 + n3 + n4) / 4}')