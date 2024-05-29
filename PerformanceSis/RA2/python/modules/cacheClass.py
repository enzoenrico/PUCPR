class Cache:
    def __init__(self, size:int, associativo:bool) -> None:
        self.size:int = size
        self.mem:dict[int, int] = {}
        if associativo == False:
            for i in range(size):
                self.mem[i] = -1
        return

    def toStr(self) -> str:
        return self.mem.__str__()
    
    