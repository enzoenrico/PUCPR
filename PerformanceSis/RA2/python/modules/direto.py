def inicializar_cache(tam_cache):
    cache = {}
    for i in range(tam_cache):
        cache[i] = -1
    return cache

def imprimir_cache(cache):
    print(f"{'Tamanho da Cache: ':<15} {len(cache):<15}")
    print(f"{'Bloco':<15} | {'Pos Memória':<15}")
    print("-" * 30)
    for posicao, valor in cache.items():
        print(f"{posicao:<15} | {valor:<15}")
    print()



def mapeamento_direto(tam_cache, pos_memoria):
    cache = inicializar_cache(tam_cache)
    print("Cache Inicial")
    imprimir_cache(cache)

    hits = 0
    misses = 0

    for i in range(len(pos_memoria)):
        pos_cache = pos_memoria[i] % tam_cache

        print(f"Linha {i} | Posição da memória desejada {pos_memoria[i]}")

        if cache[pos_cache] == pos_memoria[i]:
            hits += 1
            print("Status: Hit")
        else:
            misses +=1
            print("Status: Miss")
            cache[pos_cache] = pos_memoria[i]
        
        imprimir_cache(cache)

    totalAcesso = misses + hits
    taxaAcerto = (hits / totalAcesso) * 100
    print(f"Conectividade em Sistemas Ciberfísicos - Mapeamento Direto")
    print(f"Total de acessos: {totalAcesso}")
    print(f"Total de Misses: {misses}")
    print(f"Total de Hits: {hits}")
    print(f"Taxa de acertos (hits): {taxaAcerto :.2f}%")

# mapeamento_direto(5, [33,3,11,5])     
# mapeamento_direto(5, [0,1,2,3,4,5,6])     
# mapeamento_direto(4, [0,1,2,2,22,32,42,20,1,10,11,12,13])     
# mapeamento_direto(5, [1,6,1,11,1,16,1,21,1,26])     
# mapeamento_direto(4, [3,7,11,15,3,19,11])   
# mapeamento_direto(12, [0, 4, 8, 12, 16, 20, 24, 1, 5, 9, 13, 17])     