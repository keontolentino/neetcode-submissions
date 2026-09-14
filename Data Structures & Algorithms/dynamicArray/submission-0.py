class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.length = 0
    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        val = self.arr[self.length - 1]
        self.length -= 1
        return val

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        arr2 = [0] * (self.capacity)
        for i in range(self.length):
            arr2[i] = self.arr[i]
        self.arr = arr2
        
                
    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity