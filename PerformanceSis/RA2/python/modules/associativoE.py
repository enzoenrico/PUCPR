import cacheClass as cache


class Associativo(cache.Cache):
    def __init__(self, size: int, conj: int) -> None:
        super().__init__(size, True)
        self.conj = conj

        for i in range(self.size // conj):
            self.mem[i] = [-1] * conj
        return

    def __summary(self, hits: int, misses: int):
        print("[SUMMARY]")
        for conj, lines in self.mem.items():
            print(f"{conj} | {str(lines)}")
            print("-" * 20)
        print()

    def update_lru(self, lru: list[int], block: int) -> None:
        if block in lru:
            lru.remove(block)
        lru.append(block)
        return

    def associative_mapping_conj(self, pos: list[int]) -> None:
        print(self.toStr())
        hits, misses = 0, 0
        lru = {i: [] for i in self.mem.keys()}
        for i in range(len(pos)):
            pos_conj = (pos[i] // self.conj) % (self.size // self.conj)
            line = pos[i] % self.conj
            print(f"Line {i} | Memory Position {pos[i]}")
            if pos[i] in self.mem[pos_conj]:
                hits += 1
                print("[HIT]")
                self.update_lru(lru[pos_conj], pos[i])
            else:
                misses += 1
                print("[MISS]")
                if -1 in self.mem[pos_conj]:
                    index = self.mem[pos_conj].index(-1)
                    self.mem[pos_conj][index] = pos[i]
                else:
                    block_replaced = lru[pos_conj].pop(0)
                    index = self.mem[pos_conj].index(block_replaced)
                    self.mem[pos_conj][index] = pos[i]
                self.update_lru(lru[pos_conj], pos[i])
        print(self.__summary(hits, misses))
        return
