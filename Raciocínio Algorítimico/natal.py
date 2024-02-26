def drawTree(n):
    middle = int(n - 1)
    for i in range(n):
        print((n - i) * " ", (i*2)*"*")
    print( middle * " ", "I")
cols = int(input('insira o numero de colunas:\n'))
drawTree(cols)