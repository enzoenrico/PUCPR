def main():
    tipo_media = input(
        "[+]Escolha o tipo de média (A para aritmética, P para ponderada): ")

    if tipo_media.lower() == "a":
        notas = []
        quantidade = int(input("[+]Digite a quantidade de notas: "))

        for i in range(quantidade):
            nota = float(input(f"Digite a nota {i + 1}: "))
            notas.append(nota)

        media = sum(notas) / quantidade

    elif tipo_media.lower() == "p":
        notas = []
        pesos = []
        quantidade = int(input("[+]Digite a quantidade de notas: "))

        for i in range(quantidade):
            nota = float(input(f"Digite a nota {i + 1}: "))
            peso = float(input(f"Digite o peso da nota {i + 1}: "))
            notas.append(nota)
            pesos.append(peso)

        soma_produtos = sum([nota * peso for nota, peso in zip(notas, pesos)])
        soma_pesos = sum(pesos)
        media = soma_produtos / soma_pesos

    print(f"A média final é: {media:.2f}")

    opcao = input("[+]Deseja calcular quanto falta para passar? (S/N): ")

    if opcao.lower() == "s":
        quantidade_faltante = int(
            input("[+]Digite a quantidade de notas faltantes (deve ser 1): "))
        nota_faltante = float(input("[+]Digite o valor da nota faltante: "))
        media_necessaria = float(
            input("[+]Digite a média necessária para aprovação: "))

        soma_notas_atuais = sum(notas) + nota_faltante
        quantidade_total = quantidade + quantidade_faltante
        media_atual = soma_notas_atuais / quantidade_total

        nota_necessaria = media_necessaria * quantidade_total - sum(notas)

        print(
            f"[!]Você precisa de {nota_necessaria:.2f} na nota faltante para atingir a média necessária.")

main()
