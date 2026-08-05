class MyHashMap:

    def __init__(self):
        self.HashMap = []

    def put(self, key: int, value: int) -> None:
        for i, item in enumerate(self.HashMap):
            if key == item[0]:
                self.HashMap[i][1] = value
                return
        
        self.HashMap.append([key, value])

    def get(self, key: int) -> int:
        for i, item in enumerate(self.HashMap):
            if key == item[0]:
                return item[1]
        
        return -1

    def remove(self, key: int) -> None:
        for i, item in enumerate(self.HashMap):
            if key == item[0]:
                self.HashMap.remove(item)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)