binstr = input('Insira o número para identificação:\n')
binpat = input('Insira a sequencia desejada:\n')

# binstr = "10010100"
# binpat = "1010"

# Usar 2 ponteiros, um para a lista de binarios e outro para o padrao
# Avançar ponteiro bin, caso padrao nao seja reconhecido avançar pont bin e reiniciar pont padrao
# Caso ponteiro bin e ponteiro padrao sejam iguais, avançar os 2

pointer_pat = 0
res = []

No_num_err = "O padrão selecionado não foi encontrado no numero"

for i in range(len(binstr)):
    # Checar se o numero de indice i = ao item do padrao definid
    if binstr[i] == binpat[pointer_pat]:
        pointer_pat += 1
        res.append(i)
        if pointer_pat == len(binpat) or res == binpat:
            print(res)
            break
    else:
        pointer_pat = 0
        res.clear()

    if i >= len(binstr):
        res.clear()
        print(No_num_err)
print(res)