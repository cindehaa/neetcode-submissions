class DynamicArray:
    
    def __init__(self, capacity: int):
        self.dyn_arr = []
        self.capacity = capacity


    def get(self, i: int) -> int:
        return self.dyn_arr[i]


    def set(self, i: int, n: int) -> None:
        self.dyn_arr[i] = n

    def pushback(self, n: int) -> None:
        if len(self.dyn_arr) >= self.capacity:
            self.resize()
        
        self.dyn_arr.append(n)


    def popback(self) -> int:
        n = self.dyn_arr[len(self.dyn_arr)-1] 
        del self.dyn_arr[len(self.dyn_arr)-1] 
        return n
 

    def resize(self) -> None:
        self.capacity *= 2


    def getSize(self) -> int:
        return len(self.dyn_arr)
        
    
    def getCapacity(self) -> int:
        return self.capacity
