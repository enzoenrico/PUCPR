import cacheClass as cache


class Direto(cache.Cache):
    def __init__(self, size: int) -> None:
        super().__init__(size, False)
        return

    def mapeamento_direto(self, pos: list[int]) -> None:
        print(self.toStr())
        hits, misses = 0, 0
        for i in range(len(pos)):

            sel_pos = i % self.size
            print(sel_pos)

            if self.mem[sel_pos] == pos[i]:
                print("[HIT]")
                hits += 1
            else:
                print("[MISS]")
                self.mem[sel_pos] = pos[i]
                misses += 1
            print(self.mem)
        print(self.__summary(hits, misses))
        return

    def __summary(self, hits: int, misses: int) -> str:
        total_accesses = hits + misses
        hit_rate = hits / total_accesses if total_accesses > 0 else 0
        return f"Total Accesses: {total_accesses}\n Hits: {hits}\n Misses: {misses}\n Hit Rate: {hit_rate}"
