class Cache:
    def __init__(self, size:int) -> None:
        self.size:int = size
        self.mem:dict[int, int] = {}
        for i in range(size):
            self.mem[i] = -1
        return
    def toStr(self) -> str:
        return self.mem.__str__()
    
    def mapeamento_direto(self, pos:list[int]) ->None:
        print(self.toStr())
        hits, misses = 0, 0
        for i in range(len(pos)):
    
            sel_pos = i % self.size
            print(sel_pos)
            
            if sel_pos == pos[i]:
                print("[HIT]")
                hits += 1
            else:
                print("[MISS]")
                misses += 1
            self.mem[sel_pos] = pos[i]
            print(self.mem)
        print(self.__summary(hits, misses))
        return 

    def __summary(self, hits:int, misses:int) -> str:
        total_accesses = hits + misses
        hit_rate = hits / total_accesses if total_accesses > 0 else 0
        return f"Total Accesses: {total_accesses}\n Hits: {hits}\n Misses: {misses}\n Hit Rate: {hit_rate}"


if __name__ == "__main__":
    #new cache
    c = Cache(5)

    #data for the direct mapping in a int array
    data = list(range(21))
    c.mapeamento_direto(data)

    

