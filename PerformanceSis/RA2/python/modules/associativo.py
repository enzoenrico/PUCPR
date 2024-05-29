def inicializar_cache(tam_cache, num_conj):
    cache = {}
    for i in range(tam_cache // num_conj):
        cache[i] = [-1] * num_conj
    return cache


def imprimir_cache(cache):
    print(f"{'Conjunto':<15} | {'Bloco':<15}")
    print("-" * 40)
    for conjunto, linhas in cache.items():
        print(f"{conjunto:<15} | {str(linhas):<15}")
        print("-" * 40)
    print()


def atualizar_lru(lru, bloco):
    if bloco in lru:
        lru.remove(bloco)
    lru.append(bloco)


def mapeamento_associativo_conjunto(tam_cache, num_conj, pos_memoria):
    cache = inicializar_cache(tam_cache, num_conj)
    lru = {i: [] for i in cache.keys()}

    print("Cache Inicial")
    imprimir_cache(cache)

    hits = 0
    misses = 0

    for i in range(len(pos_memoria)):
        pos_conjunto = (pos_memoria[i] // num_conj) % (tam_cache // num_conj)
        linha = pos_memoria[i] % num_conj

        print(f"Linha {i} | Posição da memória desejada {pos_memoria[i]}")

        if pos_memoria[i] in cache[pos_conjunto]:
            hits += 1
            print("Status: Hit")
            atualizar_lru(lru[pos_conjunto], pos_memoria[i])
        else:
            misses += 1
            print("Status: Miss")
            if -1 in cache[pos_conjunto]:
                index = cache[pos_conjunto].index(-1)
                cache[pos_conjunto][index] = pos_memoria[i]
            else:
                bloco_substituido = lru[pos_conjunto].pop(0)
                index = cache[pos_conjunto].index(bloco_substituido)
                cache[pos_conjunto][index] = pos_memoria[i]
            atualizar_lru(lru[pos_conjunto], pos_memoria[i])

        imprimir_cache(cache)

    total_acessos = misses + hits
    taxa_acerto = (hits / total_acessos) * 100
    print(
        f"Conectividade em Sistemas Ciberfísicos - Mapeamento Associativo por Conjunto"
    )
    print(f"Total de acessos: {total_acessos}")
    print(f"Total de Misses: {misses}")
    print(f"Total de Hits: {hits}")
    print(f"Taxa de acertos (hits): {taxa_acerto:.2f}%")


# mapeamento_associativo_conjunto(8, 2, [33,3,11,5])
# mapeamento_associativo_conjunto(4, 2, [0,1,2,3,4,5,6])
# mapeamento_associativo_conjunto(4, 2, [0,1,2,2,22,32,42,20,1,10,11,12,13])
# mapeamento_associativo_conjunto(10, 2, [0,1,2,2,22,32,42,20,1,10,11,12,13])
# mapeamento_associativo_conjunto(5, 1, [1,6,1,11,1,16,1,21,1,26])
# mapeamento_associativo_conjunto(4, 1, [3,7,11,15,3,19,11])
# mapeamento_associativo_conjunto(8, 4,[0, 8, 16, 24, 4, 12, 20, 28])
