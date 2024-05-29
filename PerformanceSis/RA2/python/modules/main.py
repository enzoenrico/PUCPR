import cacheClass
import associativoE
import diretoE

direto = diretoE.Direto(4)
direto.mapeamento_direto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

associativo = associativoE.Associativo(4, True)
associativo.associative_mapping_conj([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
