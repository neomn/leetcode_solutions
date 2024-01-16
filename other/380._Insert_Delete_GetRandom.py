class RandomizedSet:

    def __init__(self):
        self.myset = set()
        

    def insert(self, val: int) -> bool:
        if val in self.myset:
            return False
        self.myset.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.myset:
            return False
        self.myset.remove(val)
        return True
        

    def getRandom(self) -> int:
        setlen = len(self.myset)
        return list(self.myset)[random.randint(0,setlen-1)]
