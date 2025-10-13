class LUPrefix:

    def __init__(self, n: int):
        self.id = 0
        self.stack = []

    def upload(self, video: int) -> None:
        heappush(self.stack , video)
        

    def longest(self) -> int:
        while self.stack and self.stack[0] == self.id + 1:
            self.id += 1
            heappop(self.stack)
        return self.id
        
